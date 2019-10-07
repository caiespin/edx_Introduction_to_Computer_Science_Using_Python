# -*- coding: utf-8 -*-
"""
Created on Tue May 29 17:11:37 2018

@author: Carlos Isaac
"""

import os

path =  os.getcwd()

filenames = os.listdir(path)
filenames=filenames[:276]+filenames[277:]
quarter = '_W18' 

for file in filenames:
    print(file)
    file_name, file_ext = os.path.splitext(file)
    S_name, CruzID, CommitID, = file_name.split('_')
    newname = '{}{}{}'.format(CruzID,quarter,file_ext)
    os.rename(file,newname)