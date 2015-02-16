#!/usr/bin/env python
# -*- coding: utf-8 -*-

from app import app

if __name__ == '__main__':
    app.debug = True  # 调试模式
    app.run()
