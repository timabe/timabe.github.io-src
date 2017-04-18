#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Tim Abraham'
SITENAME = u'tim abraham'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = ('%B %Y')
DEFAULT_LANG = u'en'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Feeds
FEEDS =  (('All posts', 'feeds/all.atom.xml'),
          ('Category', 'feeds/category'),
          ('OPW', 'feeds/tag/opw.atom.xml'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/timabe'),
          ('github', 'https://github.com/timabe'))


TWITTER_USERNAME = "timabe"

OUTPUT_PATH = "../blog_output/"
THEME = "themeabe"

STATIC_PATHS = [
    'images',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

# plugins
PLUGIN_PATHS = ['../pelican-plugins/']

PLUGINS = ["render_math"]

# Formatting for urls
ARTICLE_URL = "posts/{date:%Y}/{date:%m}/{slug}/"
ARTICLE_SAVE_AS = "posts/{date:%Y}/{date:%m}/{slug}/index.html"

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"


TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"

# Persistent home page
INDEX_SAVE_AS = 'pages/home.md'

RELATIVE_URLS = True

MENUITEMS = [('pies', 'https://pies.timabe.me/')]

DEFAULT_PAGINATION = 10
