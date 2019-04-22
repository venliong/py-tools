#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from MyQR import myqr
import os

ver, level, qr_name = myqr.run(
    # 参数
    words='hello world',
    # 设置容错率为最高默认边长是取决于你输入的信息的长度和使用的纠错等级；而默认纠错等级是最高级的H
    version=1,
    # 控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    level='H',
    # 用来将QR二维码图像与一张同目录下的图片相结合，产生一张黑白图片
    picture='test.jpg',
    # 控制颜色
    colorized=True,
    # 用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0。
    contrast=1.0,
    # 用来调节图片的亮度，其余用法和取值与 -con 相同
    brightness=1.0,
    # 制文件名，格式可以是 .jpg， .png ，.bmp ，.gif
    save_name=None,
    # 控制位置
    save_dir=os.getcwd()
)

print('ver={}, level={}, qr_name={}'.format(ver, level, qr_name))