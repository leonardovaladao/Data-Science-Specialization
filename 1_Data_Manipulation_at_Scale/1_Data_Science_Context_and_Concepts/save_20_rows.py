# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:35:00 2022

@author: Leonardo
"""
import sys

lines = []
with open(sys.argv[1]) as file:
    lines.extend(file.readline() for i in range(20))
    
with open(sys.argv[2], 'w') as f:
    for item in lines:
        f.write(item)
        
    