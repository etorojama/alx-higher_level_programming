#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    nulist = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return nulist
    nulist[idx] = element
    return nulist
