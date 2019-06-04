# Computable AI

This repository holds all of the source documents as well as output for [the Computable AI blog](https://computable.ai).

Any of the posts with Jupyter notebook sources can be run from here with Binder. Use the badge to launch a JupyterHub server inside the repo, and then find your post's Jupyter notebook source in `/content/{Category}`. [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/computableai/computableai.github.io/dev)

Each of the posts have a badge as well, for both Binder and Google Colab. Binder may be removed soon because it's far slower and has no GPU support.

## Development

The `dev` branch (default) contains all of the source files. The `master` branch is published by GitHub Pages, and only contains the output.

Start with `pipenv shell` to enter the virtualenv shell for this repo.

I run `make devserver` to start an auto-refreshing local server, then I run `jupyter notebook` and use Jupyter to write site content, occasionally checking the Pelican-built version of the article to make sure things look right.

When I'm done, `make publish` publishes the site (by generating a production build and using ghp-import to extract the `output/` into `master`).
