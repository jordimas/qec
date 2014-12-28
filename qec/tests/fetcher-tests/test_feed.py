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
from fetcher.feed import Feed


class TestFeed(unittest.TestCase):

    test_rss = u"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">

<channel>
  <title>W3Schools Home Page</title>
  <link>http://www.w3schools.com</link>
  <description>Free web building tutorials</description>
  <item>
    <title>Entry title 1</title>
    <link>http://www.link1.com</link>
    <description>Entry title 2</description>
  </item>
  <item>
    <title>Entry title 2</title>
    <link>http://www.link2.com</link>
    <description>Entry title 2 description</description>
  </item>
</channel>
</rss>
"""

    def test_parse_fields(self):

        feed = Feed()
        feed.parse(self.test_rss)
        entry1 = feed.entries[0]
        entry2 = feed.entries[1]

        self.assertEquals(entry1["title"], 'Entry title 1')
        self.assertEquals(entry2["title"], 'Entry title 2')
        self.assertTrue("link" not in entry1)
        self.assertTrue("link" not in entry2)

if __name__ == '__main__':
    unittest.main()
