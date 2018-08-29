# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:40:01 2018

@author: justin
"""

def replaceSpace(word, trueLen):
    for i in range(trueLen):
        print("examining:"+str(word[i]))
        if word[i] == ' ':
            for x in range(2):
                for j in range(trueLen-1, i, -1):
                    word[j] = word[j-1]
            word[i] = '%'
            word[i+1] = '2'
            word[i+2] = '0'
        
    print(word)

s = ['a', 'b', 'c', 'd',' ','','']
replaceSpace(s, 7)
