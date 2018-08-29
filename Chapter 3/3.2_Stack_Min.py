# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 22:41:42 2018

@author: justin
"""




class Stack(object):
    def __init__(self):
        self.stack = []
        self.min = []
    def pop(self):
        if len(self.stack) == 0:
            print("stack is empty, cannot pop")
            return
        x = self.stack.pop()
        if x == self.min[-1]:
            self.min.pop()
        return x
    
    def peek(self):
        return self.stack[-1]
    
    def push(self, value):
        self.stack.append(value)
        if len(self.min) == 0 or self.min[-1] > value:
            self.min.append(value)
    def isEmpty(self):
        return len(self.stack) == 0


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
s.push(-1)
s.push(0)
s.push(100)
s.push(-100)
s.push(5)