# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:36:26 2018

@author: justin
"""

def compress(word):
    consec = 0
    solution = []
    for i in range(len(word)):
        consec += 1
        if i+1 >= len(word) or word[i] != word[i+1]:
            solution.append(word[i])
            solution.append(consec)
            consec = 0
    if len(solution) > len(word):
        return word
    else:
        return solution

print(compress('aabccccca'))
print(compress('abc'))