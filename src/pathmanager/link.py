#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
define link data struct
and link depond on tools
'''
import os
import node
import pickle


class Link(object):
    def __init__(self, name, tags=None):
        self.nodes = []
        self.tags = tags
        self.name = name
    def get(self):
        return self.nodes
    def get_node(self, idx):
        return self.nodes[idx]
    def show(self):
        s = ""
        for nd in self.nodes:
            s += nd.nip
            s += "-->"
        if s != "":
            s = s[0:len(s)-3]
        return s
    def generate_scp_data(self, fname):
        f = open(fname, 'w')
        ips=""
        macs=""
        users=""
        for nd in self.nodes:
            ips += nd.nip + ","
            macs += nd.nid + ","
            users += nd.username + ","
        ips = ips[0:len(ips)-1] + '\n' 
        macs = macs[0:len(macs)-1] + '\n'
        users = users[0:len(users)-1] + '\n'

        f.write(ips)
        f.write(macs)
        f.write(users)
        f.close()
    def insert(self, lnode):
        if not isinstance(lnode, node.Node):
            raise TypeError("[Link/insert]: node is not Node type")
        self.nodes.append(lnode)
    def remove(self, lnode):
        if not isinstance(lnode, node.Node):
            raise TypeError("[Link/remove]: node is not Node type")
        self.nodes.remove(lnode)
    def update(self, lnode):
        if not isinstance(lnode, node.Node):
            raise TypeError("[Link/update]: node is not Node type")
        try:
            idx = self.nodes.index(lnode)
            self.nodes[idx] = lnode
        except ValueError:
            print("[Link/update]: can not find node in link.")

class LinkStore(object):
    def __init__(self, serial_filename):
        self.links = []
        rdir=os.path.split(os.path.realpath(__file__))[0]
        self.serial_filename = rdir + "/" + serial_filename
    def get(self, idx):
        return self.links[idx]
    def search_by_target(self, source, target):
        rt = []
        if source == None or target == None:
            print("[LinkStore/search_by_target]: source or target is None")
            return rt
        if not isinstance(source, node.Node) or not isinstance(target, node.Node):
            raise TypeError("[LinkStore/search_by_target]: source or target is not Node type")
        i = -1
        for tl in self.links:
            i += 1
            if source.nid == tl.get_node(0).nid and target.nid == tl.get_node(-1).nid:
                rt.append(i)
        return rt
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
        f.close()
    def restore(self):
        if os.path.exists(self.serial_filename) is False:
            return
        f = open(self.serial_filename, 'rb')
        self.links = pickle.load(f)
        f.close()

