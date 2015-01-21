#!/usr/bin/env python
# -*- coding: utf-8 -*-

import georgapi
import feedparser
import re
import time
import json
from datetime import datetime

polisurl="https://www.polisen.se/Vastra_Gotaland/Aktuellt/RSS/Lokal-RSS---Handelser/Lokala-RSS-listor1/Handelser-RSS---Vastra-Gotaland/?feed=rss"

feed = feedparser.parse( polisurl )

print feed[ "channel" ][ "title" ]

for item in feed[ "items" ]:
#    print row
    p = re.compile('^(\d{4})-(\d{2})-(\d{2})\ (\d{2}):(\d{2}).*?\ ([^\,]+)$')
    m = p.match(item[ "title" ])
    d = datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5)))
    addressjson = str(georgapi.addressToLatLon(m.group(6).encode("utf8")))
    print addressjson
    address = json.loads(addressjson)
    print address
    time.sleep(2)


