# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:35:10 2018

@author: justin
"""

#Implement alg to determine if string has all unique chars.


def detUnique(word):
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True


test = 'abcdefg'
test2 = 'abcdefgabc'

print(detUnique(test))
print(detUnique(test2))


def detUnique2(word):
    s = set()
    for i in word:
        if i not in s:
            s.add(i)
        else:
            return False
    return True

print(detUnique2(test))
print(detUnique2(test2))