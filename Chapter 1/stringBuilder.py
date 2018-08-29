# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:30:36 2018

@author: justin
"""

#implement string builder that takes O(n)

class stringBuilder(object):
    def __init__(self):
        self.arr = []
        
    def joinWords(self, wordlist):
        x = wordlist.split()
        for word in x:
            self.arr.append(word)
    
    def getStrings(self):
        return self.arr



wordL = "I am not a robot"

s = stringBuilder()
s.joinWords(wordL)
result = s.getStrings()
print(result)