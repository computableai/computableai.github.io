# Computable AI

This repository holds all of the source documents as well as output for [the Computable AI blog](https://computable.ai).

## Development

Computable AI is powered by [Pelican](http://docs.getpelican.com/en/stable/), a powerful static site generator.
There are many static site generators, but Pelican was chosen in support of blogging via Jupyter.

We use [Pipenv](https://docs.pipenv.org/en/latest/) for managing Python dependencies.
TL;DR:

```
pip install pipenv
pipenv install
```

The `dev` branch (default) contains all of the source files. The `master` branch is published by GitHub Pages, and only contains the output.

Start with `pipenv shell` to enter the virtualenv shell for this repo.

Run `make devserver` to start an auto-refreshing local server hosting the site at [http://localhost:8000](http://localhost:8000), then run `jupyter notebook` and use Jupyter to write site content in `content/`, occasionally checking the Pelican-built version of the article to make sure things look right.

Look at an existing post's source to see how metadata works (each source notebook has some YAML in its first cell).

Here's some example metadata. Only the first four keys are required. The default category is "Miscellany". The default image is the first image found in your post. The default status is published.

```
- title: Title of this post
- summary: The summary/subtitle of this post
- author: Joe Blogger
- date: 2019-03-03
- category: Example
- image: /images/someimage.png
- status: draft
```

Images can be right-justified, left-justified, or centered by appending, e.g., `#right` to a source url in `img` tag src.


When I'm done, `make publish` publishes the site (by generating a production build and using ghp-import to extract the `output/` into `master`).
