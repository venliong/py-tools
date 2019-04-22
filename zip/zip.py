#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zipfile

txt = open('dict.txt', 'r')
zf = zipfile.ZipFile('xx.zip')
for line in txt.readlines():
    password = line.strip()
    try:
        zf.extractall(pwd=password.encode("ascii"))
        print(password)
        exit(0)
    except Exception as e:
        print(e)
