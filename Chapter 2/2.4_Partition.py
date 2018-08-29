# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 23:34:01 2018

@author: justin
"""


from LinkedList import LinkedList, Node

def partition(ll, val):
    ret = LinkedList()

    curr = ll.head
    
    while curr != None:
        x = curr.getData()
        if x < val:
            #ll.remove(x)
            ret.insertAtHead(x)
        else:
            #ll.remove(x)
            ret.insertAtTail(x)
        curr = curr.getNext()
        
    return ret



l = LinkedList()
for i in range(20):
    l.insertAtHead(randint(1, 5))
    
print(l)

print(partition(l, 4))