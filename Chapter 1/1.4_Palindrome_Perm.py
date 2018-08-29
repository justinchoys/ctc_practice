# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 15:06:36 2018

@author: justin
"""

#check if string is permutation of palindrom
#concept: dict of palindrome has all values even, or all even except for one 1

def palinCheck(word):
    d = {}
    new_word = word.replace(" ","")
    for i in new_word:
        if i not in d.keys():
            d[i] = 1
        else:
            d[i] += 1

    seen1 = False

    
    for key in d.keys():
        if d[key] % 2 == 0:
            continue
        elif not seen1:
            seen1 = True
        else:
            return False
    return True



s = 'racecar' #hello apple '
print(palinCheck(s))