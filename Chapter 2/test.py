# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:37:12 2018

@author: justin
"""

def get_all_subsets(some_list):
    """Returns all subsets of size 0 - len(some_list) for some_list"""
    if len(some_list) == 0:
        # If the list is empty, return the empty list
        return [[]]
    subsets = []
    first_elt = some_list[0]
    rest_list = some_list[1:]
    # Strategy: Get all the subsets of rest_list; for each
    # of those subsets, a full subset list will contain both
    # the original subset as well as a version of the subset
    # that contains first_elt

    for partial_subset in get_all_subsets(rest_list): #recursive
        subsets.append(partial_subset) #to blank subset, add each partial_subset element (this is the powerset for some_list[1:], some_list[2:]...)
        next_subset = partial_subset[:] + [first_elt] #for each partial_subset element, add first-elt (which wasn't included before)
        subsets.append(next_subset) #add to subset each partial_subset+first_elt
    return subsets


print(get_all_subsets([1, 2, 3]))