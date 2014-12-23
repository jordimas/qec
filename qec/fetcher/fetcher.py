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

import os
import logging
from feed import Feed


def init_logging():
    logfile = 'fetcher.log'

    if os.path.isfile(logfile):
        os.remove(logfile)

    logging.basicConfig(filename=logfile, level=logging.DEBUG)
    logger = logging.getLogger('')
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    logger.addHandler(console)

if __name__ == '__main__':

    init_logging()

    feeds_urls = [
        "http://www.vilaweb.cat/rss/vilaweb.rss",
        "http://www.elperiodico.cat/ca/rss/rss_portada.xml"
    ]

    for url in feeds_urls:
        feed = Feed()
        feed.parse(url)
        entries = feed.entries
        for entry in entries:
            print (entry)
