# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:16:45 2018

@author: justin
"""

def oneDiff(word1, word2):
    if len(word1) - len(word2) > 1:
        return False
    elif len(word1) == len(word2):
        return checkReplace(word1, word2)
    else:
        return checkInsert(word1, word2)
    

def checkReplace(word1, word2):
    
    flag = False
    
    for i in range(len(word1)):
        if word1[i] != word2[i] and not flag:
            flag = True
        if word1[i] != word2[i] and flag:
            return False
    return True
    
def checkInsert(word1, word2):
    
    flag = False
    
    if len(word1) > len(word2):
        longer = word1
        shorter = word2
    else:
        longer = word2
        shorter = word1
    
    index1 = 0
    index2 = 0
    
    while index1 < len(shorter) and index2 < len(longer):
        if longer[index2] != shorter[index1] and not flag:
            flag = True
            index2 += 1
        if longer[index2] != shorter[index1] and flag:
            return False
        index1 += 1
        index2 += 1
    return True


s1 = 'pale, ale'
s2 = 'pale, bale'

print(oneDiff(s1, s2))


    
    