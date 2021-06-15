# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 09:01:13 2021

@author: subha
"""

import sys     # we need this library to deal with operating system

filename = sys.argv[1]

infile = open(filename)

for line in infile:
    print(line,end="") # the file has "\n" at the end of each line already

infile.close()