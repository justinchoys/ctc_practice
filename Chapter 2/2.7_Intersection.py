# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 00:05:33 2018

@author: justin
"""

from LinkedList import LinkedList, Node

def intersect(l1, l2):
    h1 = l1.head
    h2 = l2.head
    len1 = l1.size()
    len2 = l2.size()
    if len1 < len2:
        shorter = h1
        longer = h2
    else:
        shorter = h2
        longer = h1
    
    for i in range(abs(len1-len2)):
        longer = longer.getNext()
    
    while shorter != None and shorter is not longer:
        shorter = shorter.getNext()
        longer = longer.getNext()
    
    if shorter == None:
        return False
    else:
        return True


l1 = LinkedList()
l1.insertAtHead(6)
l1.insertAtHead(1)
l1.insertAtHead(7)
l1.insertAtHead(7)
l1.insertAtHead(1)
l1.insertAtHead(6)

l2 = LinkedList()
l2.insertAtHead(1)
l2.insertAtHead(2)
l2.insertAtHead(2)
l2.head.getNext().getNext().setNext(l1.head.getNext().getNext().getNext().getNext())

#l1 and l2 intersect at second 7 in l1
#l1 = 6 1 7 7 1 6
#l2 = 2 2 1 7 1 6


print(l1)
print(l2)
print(intersect(l1, l2))