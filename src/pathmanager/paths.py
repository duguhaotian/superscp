#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
define paths 
and paths depond on tools
'''
import linkStore 
import Node

class paths(object):
    def __init__(self):
        self.store = linkStore('.paths.data')
    def insert(self, link):
        self.store.insert(link)
    def remove(self, link):
        self.store.remove(link)
    def update(self, idx, link):
        self.store.update(idx, link)
    def store(self):
        self.store.store()
    def restore(self):
        self.store.restore()

if __name__ == '__main__':
    nodes = {}
    p = paths()
    n1 = Node() 
    
    

