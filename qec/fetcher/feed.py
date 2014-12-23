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

import logging
import feedparser


class Feed(object):

    def __init__(self):
        self._entries = []

    @property
    def entries(self):
        '''
            Returns a list of feed. Every feed is a dictionary with a key
            value
        '''
        return self._entries

    def parse(self, url):

        self._entries = []

        d = feedparser.parse(url)

        # Feed data
        #   list
        #       feedparser.FeedParserDict (headers, updated, encoding, entries)
        #           feedparser.FeedParserDict (entry: published, title, etc)
        #

        entries = d["entries"]
        FIELDS = ["title", "published"]

        for entry in entries:
            entry_store = {}
            for value in entry:
                if value in FIELDS:
                    msg = 'Feed value {0}:{1}'.format(value, entry[value])
                    logging.debug(msg)

                    entry_store[value] = entry[value]

            if len(entry_store) > 0:
                self._entries.append(entry_store)
