#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2026 Blagovest Petrov <blagovest@petrovs.info>
# SPDX-License-Identifier: GPL-2.0-or-later
"""Turns the saved copy of the undertype-users list into site pages and an mbox.

The list lived at Gna!, which is gone; mail-archive.com has the only copy of it.
archive/undertype-users/raw/ holds its pages as they were downloaded, and this
script reads nothing else:

  content/history/mailing-list/<n>.md     one page per message
  static/history/undertype-users.mbox     the whole list, for a mail client

Run it from the top of the repository after changing the raw copy.
"""

import email.utils
import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "archive" / "undertype-users" / "raw"
PAGES = ROOT / "content" / "history" / "mailing-list"
MBOX = ROOT / "static" / "history" / "undertype-users.mbox"
ORIGIN = "https://www.mail-archive.com/undertype-users@gna.org/"


def field(pattern, text):
    match = re.search(pattern, text, re.S)
    return html.unescape(match.group(1)).strip() if match else ""


def thread_key(subject):
    """The subject without list tag and Re:/Fwd: prefixes, which is what a thread shares."""
    subject = re.sub(r"\[Undertype-users\]", "", subject, flags=re.I)
    while True:
        stripped = re.sub(r"^\s*(re|fwd?|aw)\s*(\[\d+\])?\s*:\s*", "", subject, flags=re.I)
        if stripped == subject:
            return " ".join(subject.split()).lower()
        subject = stripped


def clean_body(body):
    """The message HTML without mail-archive.com's links, which point nowhere here."""
    # Addresses are hidden by Cloudflare as "[email protected]"; keep them hidden.
    body = re.sub(r'<a[^>]*href="/cdn-cgi/[^"]*"[^>]*>(.*?)</a>',
                  lambda m: re.sub(r"<[^>]+>", "", m.group(1)), body, flags=re.S)
    body = re.sub(r'<span class="__cf_email__"[^>]*>(.*?)</span>', r"\1", body, flags=re.S)
    body = re.sub(r'href="msg(\d{5})\.html"', r'href="../\1/"', body)
    body = re.sub(r"<blockquote[^>]*>", "<blockquote>", body)
    # Search links and the one attachment (a PGP signature): keep the text only.
    body = re.sub(r"<img[^>]*>", "", body)
    body = re.sub(r'<a[^>]*href="(/search[^"]*|msg\d{5}/[^"]*)"[^>]*>(.*?)</a>', r"\2", body, flags=re.S)
    tags = set(re.findall(r"</?([a-z]+)", body))
    assert tags <= {"pre", "p", "a", "blockquote", "tt", "strong", "em", "br"}, tags
    return body.strip()


def plain_text(body):
    text = re.sub(r"</?(pre|blockquote|p|br)[^>]*>", "\n", body)
    text = html.unescape(re.sub(r"<[^>]+>", "", text))
    return re.sub(r"\n{3,}", "\n\n", text).strip("\n")


def read_messages():
    messages = []
    for path in sorted(RAW.glob("msg*.html")):
        page = path.read_text(encoding="utf-8")
        body = re.search(r"<!--X-Body-of-Message-->(.*?)</div>", page, re.S).group(1)
        date = email.utils.parsedate_to_datetime(field(r'<span class="date"><a[^>]*>([^<]*)', page))
        subject = field(r'<span itemprop="name">([^<]*)</span></a></span>\s*</h1>', page)
        messages.append({
            "number": path.stem[3:],
            "subject": subject,
            "author": field(r'itemtype="http://schema.org/Person"><span itemprop="name">([^<]*)', page),
            "date": date,
            "msgid": field(r'name="msgid" value="([^"]*)"', page),
            "body": clean_body(body),
        })
    return messages


def main():
    messages = read_messages()

    # A thread is named after its first message, and sorted by it.
    first = {}
    for message in sorted(messages, key=lambda m: m["date"]):
        message["thread"] = first.setdefault(thread_key(message["subject"]), message["number"])

    PAGES.mkdir(parents=True, exist_ok=True)
    for old in PAGES.glob("[0-9]*.md"):
        old.unlink()
    for message in messages:
        front = {
            "title": message["subject"],
            "date": message["date"].isoformat(),
            "author": message["author"],
            "thread": message["thread"],
            "original": ORIGIN + "msg" + message["number"] + ".html",
            "url": "/history/mailing-list/" + message["number"] + "/",
            # Hugo does not read HTML content files; the layout prints this as it is.
            "body": message["body"],
        }
        lines = ["---"] + [f"{key}: {json.dumps(value, ensure_ascii=False)}" for key, value in front.items()]
        lines += ["---", ""]
        (PAGES / (message["number"] + ".md")).write_text("\n".join(lines), encoding="utf-8")

    MBOX.parent.mkdir(parents=True, exist_ok=True)
    with MBOX.open("w", encoding="utf-8", newline="\n") as mbox:
        for message in sorted(messages, key=lambda m: m["date"]):
            text = re.sub(r"^(>*From )", r">\1", plain_text(message["body"]), flags=re.M)
            mbox.write(f"From undertype-users@gna.org {message['date'].strftime('%a %b %d %H:%M:%S %Y')}\n")
            mbox.write(f"From: {message['author']}\n")
            mbox.write(f"Date: {email.utils.format_datetime(message['date'])}\n")
            mbox.write(f"Subject: {message['subject']}\n")
            if message["msgid"]:
                mbox.write(f"Message-ID: <{message['msgid']}>\n")
            mbox.write("List-Id: undertype-users.gna.org\n")
            mbox.write("Content-Type: text/plain; charset=utf-8\n\n")
            mbox.write(text + "\n\n")

    print(f"{len(messages)} messages in {len(set(m['thread'] for m in messages))} threads")


if __name__ == "__main__":
    main()
