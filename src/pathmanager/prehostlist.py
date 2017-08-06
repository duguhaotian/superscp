#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
define depond on host relationship
and relate tools
'''
import Node


class Pair(object):
    'define relationship node data'
    def __init__(self, prehost, host):
        if not isinstance(prehost, Node) or not isinstance(host, Node):
            print("prehost and host need Node type")
            return
        self.prehost = prehost
        self.host = host

class PrehostMap(object):
    def __init__(self):
        self.dmap = {}
        self.dset = {}
    def insert_pair(self, pair):
        self.dmap[pair.host.nid] = pair
        if self.dset.__contains__(pair.host.nip):
            self.dset[pair.host.nip].append(pair.host.nid)
        else:
            self.dset[pair.host.nip] = [pair.host.nid]
    def save_data(self):
        pass
    