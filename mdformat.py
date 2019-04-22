#!/usr/bin/env python3
# -*- coding: utf-8 -*-


'''
   #文件名：mdFormat.py
   本脚本用来 给MD文档生成标签头
    ---
    title: title
    date: 2018-12-25 10:36:24
    tags: tags
    categories: author
    ---
'''

import os
import time


def format_md(path, tags, categories):
    listdir = os.listdir(path)
    for file in listdir:
        if file.endswith('.md'):
            cpath = os.path.join(path, file)
            with open(cpath, 'r+', encoding='utf-8') as f:
                old = f.read()
                f.seek(0)
                f.write(r'---' + "\n")
                f.write(r'title: ' + file[0:len(file) - 3] + "\n")
                f.write(r'date: ' + time.strftime('%Y-%m-%d %H:%M:%S') + "\n")
                f.write(r'tags: ' + tags + "\n")
                f.write(r'categories: ' + categories + "\n")
                f.write(r'---' + "\n")
                f.write("\n")
                f.write(old)
                f.close()


if __name__ == '__main__':
    path = input('path=')
    tags = input('tags=')
    categories = input('categories=')
    format_md(path, tags, categories)