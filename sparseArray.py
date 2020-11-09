# -*- coding: utf-8 -*-
"""
@author: Anis
"""


class MatchingString:
    def __init__(self, filePathOfString):
        self.filePathOfStrings = filePathOfString
        self.strings = self.createStrings()

    def createStrings(self):
        strings = [line.strip() for line in open(self.filePathOfStrings, 'r')]
        print('Strings: ', strings)
        return strings

    def matchingStringsMethod(self, queries):
        """
        The function return a dict representing the frequency of occurrence of each query string in strings
            ------
        parameters:
        string strings[n] - an array of strings to search
        string queries[q] - an array of query strings
            ------
        Returns:
        resDict: a dict of results for each query its occurrence frequency
        """
        resDict = {}
        res = [self.strings.count(query) for query in queries]
        resDict = {queries[i]: res[i] for i in range(len(queries))}
        print("resDict = ", resDict)
        print("res:", res)
        return resDict
