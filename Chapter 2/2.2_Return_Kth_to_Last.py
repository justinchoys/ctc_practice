# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 23:18:58 2018

@author: justin
"""

from LinkedList import LinkedList, Node




def kthToLast(ll, k):
    curr = ll.head
    temp = curr
    for i in range(k):
        temp = temp.getNext()
    
    #now curr at head, temp at kth node
    
    while temp != None:
        temp = temp.getNext()
        curr = curr.getNext()
    
    return curr.getData()
        


l = LinkedList()
for i in range(20):
    l.insertAtHead(randint(1, 5))
    
print(l)

print(kthToLast(l, 3))