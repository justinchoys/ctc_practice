# -*- coding: utf-8 -*-
"""
Created on Mon Aug 20 23:53:19 2018

@author: justin
"""

from LinkedList import LinkedList, Node

def isPalindrome(ll):
    curr = ll.head
    s = {}
    
    while curr != None:
        x = curr.getData()
        if x not in s:
            s[x] = 1
        else:
            s[x] = s[x] + 1
        curr = curr.getNext()
    
    one_count = 0
    
    for key in s.keys():
        if s[key] % 2 == 1 and s[key] > 1:
            return False
        elif s[key] == 1:
            one_count += 1
            if one_count == 2:
                return False
    
    return True    







l1 = LinkedList()
l1.insertAtHead(6)
l1.insertAtHead(1)
l1.insertAtHead(7)
l1.insertAtHead(7)
l1.insertAtHead(1)
l1.insertAtHead(6)


print(isPalindrome(l1))