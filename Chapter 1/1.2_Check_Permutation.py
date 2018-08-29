# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:02:54 2018

@author: justin
"""

def checkPerm(word1, word2):
    d = {}
    for i in word1:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1
    
    for i in word2:
        if i not in d:
            return False
        elif d[i] == 0:
            return False
        else:
            d[i] += -1
    return True

s1 = 'banana'
s2 = 'anaban'

print(checkPerm(s1, s2))