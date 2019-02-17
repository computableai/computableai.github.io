#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Daniel Cox'
SITENAME = 'Computable AI'
SITEURL = ''
DESCRIPTION = 'Computable AI is a learning resource for aspiring AI researchers and practitioners specializing in Deep Reinforcement Learning.'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

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
PLUGIN_PATHS = ['./plugins', './plugins/pelican-plugins']
PLUGINS = ['ipynb.markup']
IPYNB_USE_METACELL = True
ARTICLE_URL = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
ARTICLE_SAVE_AS = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}.html'
DEFAULT_METADATA = {
    'status': 'draft',
    }
IGNORE_FILES = ['.ipynb_checkpoints']
USE_FOLDER_AS_CATEGORY = True

THEME = 'themes/mg'
TAG_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
DIRECT_TEMPLATES = ('index', 'categories', 'archives', 'search', 'tipue_search')
TIPUE_SEARCH_SAVE_AS = 'tipue_search.json'

SOCIAL = (('twitter', 'https://twitter.com/computableai'),
	  ('github', 'https://github.com/computableai'),)
SHARE = True

FOOTER = 'Copyright © 2019 Daniel Cox. All rights reserved.'
