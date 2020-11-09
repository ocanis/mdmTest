# -*- coding: utf-8 -*-
"""
@author: Anis
"""
from sparseArray import *
import sys

if __name__ == '__main__':
    # collection of input strings & a collection of query strings
    queries = sys.argv[1:]
    print("Queries : ", queries)
# set strings file path
    filePath = "strings.txt"

# Creating Mathcing String object
    matchingstrings = MatchingString(filePath)
    print("--------------------OUTPUT--------------------")
    # testing the method
    matchingstrings.matchingStringsMethod(queries)
