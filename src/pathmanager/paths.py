#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
define paths 
and paths depond on tools
'''
import link 

lstore = link.LinkStore('.paths.data')

def generate_scp_data(path, fname):
    path.generate_scp_data(fname)
def get(idx):
    return lstore.get(idx)
def search(path=None, tags=None):
    return lstore.search(path, tags)
def search_by_target(source, target):
    return lstore.search_by_target(source, target)
def insert(path):
    lstore.insert(path)
def remove(path):
    lstore.remove(path)
def update(idx, path):
    lstore.update(idx, path)
def store():
    lstore.store()
def restore():
    lstore.restore()

