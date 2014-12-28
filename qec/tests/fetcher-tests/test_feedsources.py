#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright (c) 2014 Jordi Mas i Hernandez <jmas@softcatala.org>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

import unittest
from fetcher.feedsources import FeedSources


class TestFeedSources(unittest.TestCase):

    test_yaml = u"""
feeds:
    - url: http://www.vilaweb.cat/rss/vilaweb.rss
    - url: http://www.elperiodico.cat/ca/rss/rss_portada.xml
"""

    def test_read_fields(self):

        feed_sources = FeedSources()
        feed_sources._read_str(self.test_yaml)
        urls = feed_sources.urls

        self.assertEquals(urls[0], 'http://www.vilaweb.cat/rss/vilaweb.rss')

if __name__ == '__main__':
    unittest.main()
