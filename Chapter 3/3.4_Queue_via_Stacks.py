# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:01:15 2018

@author: justin
"""
from stack import *

class myQueue(object):
    def __init__(self):
        self.q1 = Stack()
        self.q2 = Stack()
        self.flipped = False #false means we need to transfer q1 to q2 and pop last q1, true means we can just pop from q2
        
        
    def enqueue(self, value):
        if self.flipped:
            while self.q2.getSize() > 0:
                temp = self.q2.pop()
                self.q1.push(temp)
            self.q1.push(value)
            self.flipped = False
        else:
           self.q1.push(value)
        
        print("enqueued {0}".format(value))        
        
    def dequeue(self):
        if self.isEmpty():
            print("both stacks emptpy, cannot dequeue") 
        elif self.flipped:
            return self.q2.pop()
        elif not self.flipped:
            while self.q1.getSize() > 1:
                temp = self.q1.pop()
                self.q2.push(temp)
            self.flipped = True
            return self.q1.pop()
        
    def peek(self):
        if self.isEmpty():
            print("both stacks empty, cannot peek")
        elif self.flipped:
            return self.q2.peek()
        elif not self.flipped:
            while self.q1.getSize() > 0:
                temp = self.q1.pop()
                self.q2.push(temp)
            self.flipped = True
            return self.q2.peek()
    
    def isEmpty(self):
        return self.q1.getSize() == 0 and self.q2.getSize() == 0



q = myQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(5)
print(q.dequeue())