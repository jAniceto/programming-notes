#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'José Aniceto'
SITENAME = 'Annotatio'
BIO = 'A collection of codding notes and snippets from my journey to self taught programming.'
# PROFILE_IMAGE = 'photoB&W2_square.jpg'

PATH = 'content'

TIMEZONE = 'Europe/Lisbon'
LOCALE = 'en_gb'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('user', 'joseaniceto.com'),)

# Social widget
# SOCIAL = (('Personal Page', 'http://joseaniceto.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Custom settings
TYPOGRIFY = True
THEME = 'themes/pelican-hyde-2'
HYDE_THEME = 'theme-flat'
STATIC_PATHS = ['images']
# EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
USE_FOLDER_AS_CATEGORY = True
# ARTICLE_PATHS = ['']
SLUGIFY_SOURCE = 'basename'

# Debugging
LOAD_CONTENT_CACHE = False