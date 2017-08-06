#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
this file define Node data struct
and node depond on tools
'''

class Node:
    'define Node members'

    def __init__(self, nid, nip, mask=None, hostname=None):
        self.nid = nid
        self.nip = nip
        self.mask = mask
        self.hostname = hostname
        self.tags = None
        self.describe = None
        self.prehost = None
    def set_prehost(self, prehost):
        'set node depend on host id'
        if isinstance(prehost, Node):
            self.prehost = prehost.nid
        else:
            print("prehost need Node type\n")
    def set_mask(self, mask):
        'set node ip mask'
        self.mask = mask
    def set_hostname(self, hostname):
        'set Node hostname'
        self.hostname = hostname
    def set_tags(self, tags):
        'set node tags, tags is array'
        self.tags = tags
    def set_describe(self, describe):
        'set node describe, describe good for user to know which node is it.'
        self.describe = describe
    def __eq__(self, other):
        if not isinstance(other, Node):
            raise TypeError("[Node/__eq__]: other is not Node type")
        if self.nid == other.nid and self.nip == other.nip:
            return True
        return False
