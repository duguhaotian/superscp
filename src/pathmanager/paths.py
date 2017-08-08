#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
define paths 
and paths depond on tools
'''
import link 
import node
import tool

class paths(object):
    def __init__(self):
        self.store = link.linkStore('.paths.data')
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
    print(tool.get_ip('enp1s0f1'))
    n1 = node.Node(tool.get_mac('enp1s0f1'), tool.get_ip('enp1s0f1'))
    n2 = node.Node(tool.get_mac('enp1s0f0'), tool.get_ip('enp1s0f0'))
    n3 = node.Node('58:60:5f:44:3c:b1', '10.67.188.132')
    n4 = node.Node('52:54:00:00:00:13', '192.168.122.179')
    l1 = link.Link() 
    l1.insert(n3)
    l1.insert(n4)


