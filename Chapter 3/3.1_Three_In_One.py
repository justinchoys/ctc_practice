# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 17:50:26 2018

@author: justin
"""

from stack import *

#use single array to implement three stacks
#len(arr)/3 spaces for each stack

user_input = int(input("What is length of array?"))

array = [None for i in range(user_input)]

stack_ind = (0, user_input//3, user_input//3 * 2)
stack_size = [0, 0, 0]

print("Stack sizes are {0}".format(stack_size))

def push(stackNum, value):
    if stack_size[stackNum] < user_input // 3: #there is space to add value to stack
        array[stack_ind[stackNum] + stack_size[stackNum]] = value
        stack_size[stackNum] += 1
    else:
        print("Stack {0} is full, cannot push new value".format(stackNum))

def pop(stackNum):
    if stack_size[stackNum] > 0: #there is value to pop
         ret = array[stack_ind[stackNum] + stack_size[stackNum]-1]
         array[stack_ind[stackNum] + stack_size[stackNum]-1] = None
         stack_size[stackNum] -= 1
         return ret
    else:
        print("Stack {0} is empty, cannot pop value".format(stackNum))
        
def peek(stackNum):
    return array[stack_ind[stackNum] + stack_size[stackNum]-1]

def isEmpty(stackNum):
    return stack_size[stackNum] == 0


push(0, 1)
push(0, 2)
push(0, 3)
push(0, 4)

push(1, 5)
push(1, 6)
push(1, 7)
push(1, 8)

push(2, 9)
push(2, 10)
push(2, 11)
push(2, 12)
