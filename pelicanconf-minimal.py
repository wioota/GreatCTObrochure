#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Daniel Walters'
SITENAME = 'Great CTO'
SITEURL = ''

PATH = 'content'
TIMEZONE = 'UTC'
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Theme
THEME = 'themes/cto-pro'

# URL Settings
ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

# Menu items
MENUITEMS = (
    ('Services', '/services/'),
    ('About', '/about/'),
    ('Blog', '/blog/'),
    ('Contact', '/contact/'),
)

# Social widget
SOCIAL = (
    ('LinkedIn', 'https://linkedin.com/in/danielwalters'),
    ('Twitter', 'https://twitter.com/danielwalters'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Plugins - MINIMAL SET
PLUGIN_PATHS = ['plugins']
PLUGINS = [
    'neighbors',
    'sitemap',
    # 'substack_importer',  # Disabled for reliable deployment
]

# Static paths
STATIC_PATHS = [
    'assets',
    'extras/robots.txt',
    'extras/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
}

# Sitemap configuration
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 1.0
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

# Markdown extensions
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {},
    },
    'output_format': 'html5',
}

# Display pages in menu
DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False

# Template pages
TEMPLATE_PAGES = {}

# Page variables for templates
PAGE_EXCLUDES = []
ARTICLE_EXCLUDES = []

# Direct templates
DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'archives']
PAGINATED_TEMPLATES = {
    'index': None,
    'tag': None,
    'category': None,
    'author': None,
}
