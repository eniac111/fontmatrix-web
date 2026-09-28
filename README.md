# fontmatrix.l10n-bg.dev

The website of [Fontmatrix](https://github.com/eniac111/fontmatrix), built with
[Hugo](https://gohugo.io/) and published on GitHub Pages at
<https://fontmatrix.l10n-bg.dev/>.

```
hugo server        # preview at http://localhost:1313/
hugo build --minify  # the site, in public/
```

A push to `main` builds and publishes the site (`.github/workflows/pages.yml`).

- `content/` — the pages; `content/news/` the release notes; `content/history/`
  the pages of the old fontmatrix.be website, recovered from the Internet Archive.
- `layouts/`, `assets/style.css` — the templates and the one stylesheet.
- `static/fonts/` — [Veleka World](https://github.com/eniac111/Veleka) by Stefan
  Peev, under the SIL Open Font License 1.1.
