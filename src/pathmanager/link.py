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

class Link(object):
    def __init__(self):
        self.nodes = []
        self.tags = None
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
    def store(self):
        f = open('.link.data', 'wb')
        pickle.dump(self.nodes, f)
    def restore(self):
        f = open('.link.data', 'rb')
        self.nodes = pickle.load(f)

