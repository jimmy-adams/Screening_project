# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 17:05:30 2020

@author: Melody
"""
import os

exit_code = os.system('ping www.baidu.com')
if exit_code == False:
    raise Exception('connect failed.')

