import math
import os
import random
import re
import sys

# 1st Method
# """ Nasted loops Big0 --> O(n²) quadratic time complexity"""
# def matchingStrings(strings, queries):
#    queryResult = []
#    for query in queries:
#        qCounter = 0
#
#        for string in strings:
#            if str(query) == str(string):
#                qCounter += 1
#        queryResult.append(qCounter)
#    return(queryResult)

# -------

# 2nd Method
#


def matchingStrings(strings, queries):
    return [strings.count(query) for query in queries]

# ==================


if __name__ == '__main__':
    #fptr = sys.stdout
    #os.environ['OUTPUT_PATH'] = "C:\\Users\\Anis\\Documents\\__SelfLearning__\\__MaisonDuMondeTEST\\input01.txt"
    fptr = open(
        "C:\\Users\\Anis\\Documents\\__SelfLearning__\\__MaisonDuMondeTEST", 'w')

    strings_count = int(input())

    strings = []

    for _ in range(strings_count):
        strings_item = input()
        strings.append(strings_item)

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matchingStrings(strings, queries)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
