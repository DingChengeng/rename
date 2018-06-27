# -*- coding: UTF-8 -*-
import os, sys
f=file('/home/ding/下载/name.txt')
newnames=f.readlines()
path='/home/ding/下载/xcache'
name=os.listdir(path)
name.sort()
for i in name:
    print i,

for j in range(len(newnames)):
    newnames[j]= newnames[j].replace(' ', '')
    newnames[j] = newnames[j].strip()
    print newnames[j]
os.chdir(path)
for k in range(len(name)):
    os.rename(name[k],newnames[k]+'.mp4')