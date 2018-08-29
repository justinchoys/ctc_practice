# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:47:36 2018

@author: justin
"""

from stack import *

class SetOfStack(object):
    def __init__(self):
        self.array = []
        self.limit = 3
    
    def push(self, value):
        if self.array == [] or self.array[-1].getSize() == self.limit:
            self.array.append(Stack())
        self.array[-1].push(value)
        
    def pop(self):
        if self.array == []:
            print("SetOfStack empty, cannot pop")
            return
        elif self.array[-1].getSize() == 1:
            x = self.array[-1].pop()
            self.array.pop()
            return x
        else:
            return self.array[-1].pop()
        
    def popAtIndex(self, ind):
        if ind > len(self.array) - 1:
            print("Index not valid")
            return
        elif self.array[ind].getSize() == 1:
            x = self.array[ind].pop()
            self.array.pop(ind)
            return x
        else:
            return self.array[ind].pop()
        
    
ss = SetOfStack()
ss.push(1)
ss.push(2)
ss.push(3)
ss.push(2)
ss.push(-1)
ss.push(0)
ss.push(100)
ss.push(-100)
ss.push(5)
ss.push(5)