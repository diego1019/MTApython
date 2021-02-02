# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 14:25:29 2021

@author: TQC
"""

scort=[]
while True:
    inscort=int(input("分數:"))
    if inscort=="  ":
        break
    else:
        scort.append(inscort)
        scort.sort()
        scort.reverse()
        print(scort)
    
    
