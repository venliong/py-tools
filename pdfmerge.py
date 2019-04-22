#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, codecs
from PyPDF2 import PdfFileReader, PdfFileMerger


def list_file(path):
    files = os.listdir(path)
    return [os.path.join(path, i) for i in files if not os.path.isdir(os.path.join(path, i)) and i.endswith(".pdf")]


def merge_files(path, output_filename):
    merger = PdfFileMerger()
    file_list = list_file(path)
    if len(file_list) == 0:
        print("不存在pdf文件")
        sys.exit()
    for filename in file_list:
        f = codecs.open(filename, 'rb')
        file_rd = PdfFileReader(f)
        short_filename = os.path.basename(os.path.splitext(filename)[0])
        merger.append(file_rd, bookmark=short_filename, import_bookmarks=False)
        print('合并文件：%s' % filename)
        f.close()
    out_filename = os.path.join(os.path.join(path), output_filename)
    merger.write(out_filename)
    print('输出文件：%s' % out_filename)
    merger.close()


if __name__ == "__main__":
    path = input('path=')
    output_file = input("output_file=")
    merge_files(path, output_file)
