#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if j == search else j for j in my_list]
