#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PyInstaller.__main__ import run
import pygame
font=pygame.font.Font(None,36)
font=pygame.font.SysFont('arial',36)
# -F:打包成一个EXE文件
# -w:不带console输出控制台，window窗体格式
# --paths：依赖包路径
# --icon：图标
# --noupx：不用upx压缩
# --clean：清理掉临时文件

if __name__ == '__main__':
    opts = ['-w','main.py', '--paths=C:\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\bin',
            '--paths=C:\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\plugins',
            '--icon=./ico/bug.ico','--noupx', '--clean',
            ]
    # opts = ['-F', '-w','main.py', '--paths=C:\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\bin',
    #         '--paths=C:\\Python36\\Lib\\site-packages\\PyQt5\\Qt\\plugins',
    #         '--icon=./ico/bug.ico','--noupx', '--clean',
    #         ]

    run(opts)