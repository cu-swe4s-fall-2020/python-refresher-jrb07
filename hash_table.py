'''
Provides hash tables and hash functions
'''

import sys


class Hash_Table:

    def __init__(self, size):
        self.size = size
        self.my_hash_table = [[] for _ in range(self.size)]

    def hash_function(self, string, size=None):
        if size is None:
            size = self.size
        return hash(string) % size

    def get(self, key):
        return self.my_hash_table[self.hash_function(key)]

    def put(self, key, value):
        self.my_hash_table[self.hash_function(key)].append(value)
