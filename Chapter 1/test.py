# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 12:21:42 2018

@author: justin
"""

def urlify(s1):
    s = list(s1)
    for i in range(len(s)-1):
        if s[i] == " ":
            for j in range(len(s)-1, i+1, -1):
                s[j] = s[j-2]
            s[i] = '%'
            s[i+1] = '2'
            s[i+2] = '0'
    return str(s)
    
s = 'I am here    '

t = (urlify(s))
            