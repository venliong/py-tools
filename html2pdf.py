#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pdfkit
import os

path_wk = r'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'  # 安装位置
config = pdfkit.configuration(wkhtmltopdf=path_wk)
path = r'C:\pywork\learn\tools'

listdir = os.listdir(path)
for s in listdir:
    if s.endswith(".html"):
        with open(os.path.join(path, s), 'r+', encoding='utf-8') as f:
            old = f.read()
            f.seek(0)
            f.write(r'<meta charset="utf-8">')
            f.write('''
            <style type="text/css">
                p{
                    font-size: 24px
                }
            </style>
            ''')
            f.write(old)
            f.close()


listdir = os.listdir(path)
for s in listdir:
    if s.endswith(".html"):
        with open(os.path.join(path, s), 'r', encoding='utf-8') as f:
            pdfkit.from_file(f, os.path.join(path, s[0:len(s)-5] + '.pdf'), configuration=config)
