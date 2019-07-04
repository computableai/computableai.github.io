#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'the Computable AI authors'
SITENAME = 'Computable AI'
SITEURL = 'http://localhost:8000'
SITESUBTITLE = 'A Machine Intelligence Blog'
DESCRIPTION = 'Computable AI is a machine intelligence blog from a handful of DRL practitioners, intended to crystalize, internalize, share, and explain.'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

IPYNB_SKIP_CSS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/computableai'),
          ('GitHub', 'https://github.com/computableai'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup', 'sitemap', 'representative_image']
IPYNB_USE_METACELL = True
SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
            },
        'changefreqs': {
            'articles': 'daily',
            'indexes': 'daily',
            'pages': 'monthly'
            },
        }
ARTICLE_URL = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
#DEFAULT_METADATA = {
#    'status': 'draft',
#    }
WITH_FUTURE_DATES = False
STATIC_PATHS = ['static']
EXTRA_PATH_METADATA = {
    'static/images/favicons/favicon.ico': {'path': 'favicon.ico'},
    }
IGNORE_FILES = ['.ipynb_checkpoints', 'icebox', '{static}']
#USE_FOLDER_AS_CATEGORY = True
DEFAULT_CATEGORY = 'Miscellany'

THEME = 'themes/mg'
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

SOCIAL = (('twitter', 'https://twitter.com/computableai'),
	  ('github', 'https://github.com/computableai'),)
GITHUB_URL = 'https://github.com/computableai/computableai.github.io'
TWITTER_URL = 'https://twitter.com/computableai'
TWITTER_USERNAME = 'computableai'
SHARE = True

FOOTER = 'Copyright © 2019 the Computable AI authors. All rights reserved.'

DELETE_OUTPUT_DIRECTORY = True
