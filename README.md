# Barton lab website

The site is built with [Zensical](https://zensical.org/) and published to GitHub Pages.

## Local setup

```sh
python3 -m venv .venv
.venv/bin/python -m pip install --requirement requirements.txt
```

Preview the site locally:

```sh
.venv/bin/zensical serve
```

Build the production site and validate links and configuration:

```sh
.venv/bin/zensical build --clean --strict
```

The GitHub Actions workflow in `.github/workflows/ci.yml` deploys the site after each push to `main`. The repository's Pages source must be set to **GitHub Actions**.
