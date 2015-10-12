#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os


THEME = "ydf-cern-theme" # or change to $(pwd)/ydf-cern-theme
AUTHOR = u'Alexander Baranov'
SITENAME = u'ALEPH 2015 workshop'
SITEURL = os.environ.get('SITEURL', 'http://yandexdataschool.github.io/aleph2015')
print "SITEURL: '%s'" % SITEURL

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

DISPLAY_PAGES_ON_MENU = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


STATIC_PATHS = ['images', 'pdfs', 'static']

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
