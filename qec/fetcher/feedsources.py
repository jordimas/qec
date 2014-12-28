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
import yaml


class FeedSources(object):

    def __init__(self):
        self._urls = []

    @property
    def urls(self):
        return self._urls

    def read(self, filename):
        self._urls = []
        with open(filename, 'r') as f:
            self._read_str(f)

    def _read_str(self, string):
        doc = yaml.load(string)
        feeds = doc["feeds"]
        for feed in feeds:
            url = feed["url"]
            msg = 'Feed url {0}'.format(url)
            logging.debug(msg)
            self._urls.append(url)
