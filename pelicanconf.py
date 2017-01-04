#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Tim Abraham'
SITENAME = u'tim abraham'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
DEFAULT_DATE_FORMAT = ('%B %Y')
DEFAULT_LANG = u'en'

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

MENUITEMS = [('pies', 'https://pies.timabe.me/')]

DEFAULT_PAGINATION = False

