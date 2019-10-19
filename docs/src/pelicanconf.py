#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'José Aniceto'
SITENAME = 'Annotatio'
BIO = 'A collection of codding notes and snippets from my journey to self taught programming.'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom settings
TYPOGRIFY = True
THEME = 'themes/pelican-hyde-2'
HYDE_THEME = 'theme-flat'
STATIC_PATHS = ['images']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
USE_FOLDER_AS_CATEGORY = True
# ARTICLE_PATHS = ['']
SLUGIFY_SOURCE = 'basename'
SUMMARY_MAX_LENGTH = 150

# Debugging
LOAD_CONTENT_CACHE = False