# -*- coding: utf-8 -*-
"""
Created on Wed May 23 01:27:40 2018

@author: Carlos Isaac
"""

import os

path =  os.getcwd()

filenames = os.listdir(path)
filenames=filenames[:233]+filenames[234:]

i = 0
for roots, dirs, files in os.walk(path):
    for file in files:
        if file == 'Lab4.asm':
            oldpath = os.path.join(roots,file)
            newname = filenames[i] + '.asm'
            newpath = os.path.join(path,newname)
            print(newpath)
            print(oldpath)
            os.rename(oldpath,newpath)
            i += 1
