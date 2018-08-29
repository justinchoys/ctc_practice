# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:42:51 2018

@author: justin
"""



class Stack(object):
    def __init__(self):
        self.stack = []
    
    def pop(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]
    
    def push(self, value):
        self.stack.append(value)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def getSize(self):
        return len(self.stack)

class Queue(object):
    def __init(self):
        self.stack = []
        
    def dequeue(self):
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def enqueue(self, value):
        self.stack.insert(0, value)
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    

        