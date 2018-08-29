# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 23:22:06 2018

@author: justin
"""

from LinkedList import LinkedList, Node

def deleteMiddleNode(node):
    todel = node
    while todel.getNext().getNext() != None:
        todel.setData(todel.getNext().getData())
        todel = todel.getNext()
    todel.setData(todel.getNext().getData())
    todel.setNext(None)
    

l = LinkedList()
for i in range(20):
    l.insertAtHead(randint(1, 5))
    
print(l)
deleteMiddleNode(l.head.getNext().getNext().getNext())
print(l)