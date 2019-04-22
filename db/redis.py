#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from redis import Redis

r = Redis(host='IP', port=8613)
r.set('name', 'name')
r.set('age', 22)
r.set('address', 'sz')
print(r.get('name'))
keys = r.keys()
for i in keys:
    print(i)
