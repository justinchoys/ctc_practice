# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 22:47:52 2018

@author: justin
"""

from LinkedList import LinkedList, Node
from random import *


def removeDuplicates(ll):
    
    temp = ll.head
    s = set([temp.getData()])
    while temp.getNext() != None:
        if temp.getNext().getData() in s:
            temp.setNext(temp.getNext().getNext())
        else:
            s.add(temp.getNext().getData())
            temp = temp.getNext()
    return ll






l = LinkedList()
for i in range(20):
    l.insertAtHead(randint(1, 5))
    
print(l)

print(removeDuplicates(l))



def removeDuplicates2(ll):
    temp = ll.head
    while temp != None:
        temp2 = temp
        while temp2.getNext() != None:
            if temp2.getNext().getData() == temp.getData():
                temp2.setNext(temp2.getNext().getNext())
            else:
                temp2 = temp2.getNext()
        temp = temp.getNext()

    return ll


l = LinkedList()
for i in range(20):
    l.insertAtHead(randint(1, 5))
    
print(l)

print(removeDuplicates(l))

        
        