#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
define depond on host relationship
and relate tools
'''
import Node
import pickle


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
    def store(self):
        f = open('.prehost.dmap', 'wb')
        pickle.dump(self.dmap, f)
        f = open('.prehost.dset', 'wb')
        pickle.dump(self.dset, f)
    def restore(self):
        f = open('.prehost.dmap', 'rb')
        self.dmap = pickle.load(f)
        f = open('.prehost.dset', 'rb')
        self.dset = pickle.load(f)
    
