# -*- coding: utf-8 -*-
"""
Created on Wed Aug 15 14:15:57 2018

@author: justin
"""
#implementing hash table using list of list and simple hash function (%)

HASH_TABLE_SIZE = 10

class hashTable(object):
    def __init__(self):
        self.table = [[] for x in range(HASH_TABLE_SIZE)]
    
    def hashFunction(self, num):
        return num % HASH_TABLE_SIZE
    
    def insert(self, num, data):
        self.table[self.hashFunction(num)].append((num, data))
    
    def get(self, num):
        for item in self.table[self.hashFunction(num)]:
            if item[0] == num:
                return item[1]
        
        raise Exception("Item not found in hash table")
    
        
h = hashTable()

h.insert(1, 'apple')
h.insert(11, 'banana')
h.insert(2, 'citrus')