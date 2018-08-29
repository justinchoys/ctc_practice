# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 23:45:00 2018

@author: justin
"""

from LinkedList import LinkedList, Node


def sumList(l1, l2):
    h1 = l1.head
    h2 = l2.head
    ret = LinkedList()
    carry = 0
    while h1 != None or h2 != None:    
        total = 0 + carry
        if h1 != None:
            total += h1.getData()
            h1 = h1.getNext()
        if h2 != None:
            total += h2.getData()
            h2 = h2.getNext()
            
        carry = total // 10
        print("carry is " + str(carry) + " and total is " + str(total))
        ret.insertAtTail(total%10)
        
        
        
    return ret



l1 = LinkedList()
l1.insertAtHead(6)
l1.insertAtHead(1)
l1.insertAtHead(7)


l2 = LinkedList()
l2.insertAtHead(2)
l2.insertAtHead(9)
l2.insertAtHead(5)


print(sumList(l1, l2))



l1 = LinkedList()
l1.insertAtHead(6)
l1.insertAtHead(1)
l1.insertAtHead(7)


l2 = LinkedList()
l2.insertAtHead(2)
l2.insertAtHead(9)
l2.insertAtHead(5)
l2.insertAtHead(1)

print(sumList(l1, l2))