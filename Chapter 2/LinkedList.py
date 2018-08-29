# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 16:46:43 2018

@author: justin
"""

class Node(object):
    
    def __init__(self, data = None, nextNode = None):
        self.data = data
        self.nextNode = nextNode
    
    def getNext(self):
        return self.nextNode
    
    def setNext(self, node):
        self.nextNode = node
    
    def getData(self):
        return self.data
    
    def setData(self, data):
        self.data = data

class LinkedList(object):
    def __init__(self):
        self.head = None
        
    def insertAtHead(self, data):
        node = Node(data)
        if self.head:
            node.setNext(self.head)
            self.head = node
        else:
            self.head = node
    
    def insertAtTail(self, data):
        temp = self.head
        if temp == None:
            self.insertAtHead(data)
        else:
            while temp.getNext() != None:
                temp = temp.getNext()
            temp.setNext(Node(data))
            
    def remove(self, data):
        temp = None
        curr = self.head
        if curr == None:
            raise Exception("LinkedList is empty")
        else:
            while curr != None and curr.getData() != data:
                temp = curr
                curr = curr.getNext()
        
        if curr == None:
            raise Exception("LinkedList did not contain the data to delete")
        elif temp == None and self.head.getNext() != None:
            self.head = self.head.getNext()
        elif temp == None and self.head.getNext() == None:
            self.head = None
        else:
            temp.setNext(curr.getNext())
            
            
    def size(self):
        count = 0
        curr = self.head
        
        while curr != None:
            count += 1
            curr = curr.getNext()
        
        return count
    
    def __str__(self):
        result = []
        curr = self.head
        while curr != None:
            result.append(curr.getData())
            curr = curr.getNext()
        return str(result)

