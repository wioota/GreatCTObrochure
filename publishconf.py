#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://wioota.github.io/GreatCTObrochure'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

# Analytics
# GOOGLE_ANALYTICS = "G-XXXXXXXXXX"
# PLAUSIBLE_ANALYTICS = {
#     'domain': 'your-domain.com',
#     'data_domain': 'your-domain.com'  # optional
# }

# Social
# TWITTER_USERNAME = 'yourhandle'
# LINKEDIN_URL = 'https://linkedin.com/in/yourprofile'

# SEO
# SITE_DESCRIPTION = 'Expert CTO coaching, fractional executive services, and technology consulting'
