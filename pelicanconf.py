#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'BioComp'
SITENAME = u'BioComp'
SITEURL = ''
THEME = 'theme'
PATH = 'content'
TIMEZONE = 'America/Sao_Paulo'
DEFAULT_LANG = u'pt_BR'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# INDEX_SAVE_AS = 'index-pt_BR.html'


# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),
        )


# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

LOCALE = ('pt_BR','pt_BR.UTF-8','en_US','en_US.UTF-8')
DATE_FORMATS = {
    'en_US': '%a, %d %b %Y',
    'pt_BR': '%d/%m/%Y (%a)',
}
I18N_TEMPLATES_LANG = 'pt_BR'
OG_LOCALE = 'pt_BR'


STATIC_PATHS = [
    'images',
    # 'extra/robots.txt',
    'extra/favicon.ico'
]

EXTRA_PATH_METADATA = {
    # 'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
