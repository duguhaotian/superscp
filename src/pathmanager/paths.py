#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
define paths 
and paths depond on tools
'''
import link 

lstore = link.LinkStore('.paths.data')

def insert(link):
    lstore.insert(link)
def remove(link):
    lstore.remove(link)
def update(idx, link):
    lstore.update(idx, link)
def store():
    lstore.store()
def restore():
    lstore.restore()

