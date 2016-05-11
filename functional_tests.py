#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
"""

"""

__author__ = 'Hu Chao'
__version__ = '0.0.0.0'

from selenium import webdriver

browser = webdriver.Firefox()
browser.implicitly_wait(3)
browser.get('http://localhost:8000')
#assert 'To-Do' in browser.title
#browser.quit()

if __name__ == '__main__':
    pass