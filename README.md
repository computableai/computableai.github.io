# Computable AI

This repository holds all of the source documents as well as output for [the Computable AI blog](https://computable.ai).

## Development

This repository uses [Pipenv](https://docs.pipenv.org/en/latest/) for managing Python dependencies. Take a moment to get it installed and achieve rudimentary familiarity before continuing.

TLDR;
```
pip install pipenv
pipenv install
```

The `dev` branch (default) contains all of the source files. The `master` branch is published by GitHub Pages, and only contains the output.

Start with `pipenv shell` to enter the virtualenv shell for this repo.

I run `make devserver` to start an auto-refreshing local server, then I run `jupyter notebook` and use Jupyter to write site content, occasionally checking the Pelican-built version of the article to make sure things look right.

When I'm done, `make publish` publishes the site (by generating a production build and using ghp-import to extract the `output/` into `master`).
