# Computable AI

Source for [computable.ai](https://computable.ai), built with [Quarto](https://quarto.org).

## Structure

- `posts/<slug>/index.ipynb` — blog posts, authored as Jupyter notebooks with Quarto YAML front matter in a leading raw cell
- `_icebox/` — unpublished material (drafts and retired posts); the leading underscore keeps Quarto from rendering it
- `static/images/` — images referenced by posts at `/static/images/...`
- `_quarto.yml` — site configuration
- `index.qmd` — the blog listing page
- `about.qmd` — the About page

## Writing a post

Create `posts/<slug>/index.ipynb`. The first cell must be a **raw** cell containing YAML front matter:

```yaml
---
title: "Title of this post"
description: "The summary/subtitle of this post"
author: "Daniel Cox"
date: 2026-01-01
categories: ["Some Category"]
image: /static/images/someimage.png
---
```

`image` is optional (it illustrates the post in the listing). Add `draft: true` to keep a post out of the published site while still rendering it locally.

Notebook outputs are rendered as-is; Quarto does not re-execute notebooks at build time (`execute: enabled: false`), so run the notebook yourself before committing if you want fresh outputs.

## Local preview

Install [Quarto](https://quarto.org/docs/get-started/), then:

```
quarto preview
```

## Publishing

Push to `dev`. A GitHub Actions workflow (`.github/workflows/publish.yml`) renders the site and deploys it to the `master` branch, which GitHub Pages serves at computable.ai. No manual publish step.

## History

The site was originally built with Pelican and the pelican-ipynb plugin (2019); it was migrated to Quarto in 2026. Old article URLs (`/articles/YYYY/Mon/DD/slug.html`) redirect to the new locations via Quarto aliases.
