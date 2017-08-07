#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
define link data struct
and link depond on tools
'''
import Node
import pickle

class LinkNode(object):
    'link define the way of transfer data'
    def __init__(self, host, tags=None, describe=None):
        if not isinstance(host, Node):
            raise TypeError("node type is not Node, check you parameter.")
        self.host = host
        self.tags = tags
        self.describe = describe
    def set_tags(self, tags):
        'set node tags'
        self.tags = tags
    def set_describe(self, describe):
        'set node describe'
        self.describe = describe
    def __eq__(self, other):
        if not isinstance(other, LinkNode):
            raise TypeError("[LinkNode/__eq__]: other is not LinkNode type")
        if self.host == other.host:
            return True
        return False

class Link(object):
    def __init__(self, tags=None):
        self.nodes = []
        self.tags = tags
    def insert(self, node):
        if not isinstance(node, LinkNode):
            raise TypeError("[Link/insert]: node is not LinkNode type")
        self.nodes.append(node)
    def remove(self, node):
        if not isinstance(node, LinkNode):
            raise TypeError("[Link/remove]: node is not LinkNode type")
        self.nodes.remove(node)
    def update(self, node):
        if not isinstance(node, LinkNode):
            raise TypeError("[Link/update]: node is not LinkNode type")
        try:
            idx = self.nodes.index(node)
            self.nodes[idx] = node
        except ValueError:
            print("[Link/update]: can not find node in link.")

class linkStore(object):
    def __init__(self, serial_filename):
        self.links = []
        self.serial_filename = serial_filename
    def get(self, idx):
        return self.links[idx]
    def search(self, link=None, tags=None):
        'search by tags function do not support now.'
        if not isinstance(link, Link):
            raise TypeError("[linkStore/insert]: link is not Link type")
        rt = []
        if link == None and tags == None:
            for i in range(len(self.links)):
                rt.append(i)
            return rt
        i = -1 
        for tl in self.links:
            i += 1
            if len(tl.nodes) != len(link):
                continue
            flag = True
            j = -1
            for node in tl.nodes:
                j += 1
                if node != link.nodes[j]:
                    flag = False
                    break
            if flag:
                rt.append(i)
        return rt
    def insert(self, link):
        if not isinstance(link, Link):
            raise TypeError("[linkStore/insert]: link is not Link type")
        self.links.append(link)
    def remove(self, idx):
        del self.links[idx]
    def update(self, idx, link):
        if not isinstance(link, Link):
            raise TypeError("[linkStore/update]: link is not Link type")
        try:
            self.nodes[idx] = node
        except ValueError:
            print("[linkStore/update]: can not find node in link.")
    def store(self):
        f = open(self.serial_filename, 'wb')
        pickle.dump(self.links, f)
    def restore(self):
        f = open(self.serial_filename, 'rb')
        self.links = pickle.load(f)

