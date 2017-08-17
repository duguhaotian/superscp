#!/usr/bin/python
# -*- coding: UTF-8 -*-
'''
this file define Node data struct
and node depond on tools
'''
import os
import pickle

node_map = {}
rdir=os.path.split(os.path.realpath(__file__))[0]
if os.path.exists(rdir) is False:
    os.makedirs(rdir)
serial_filename=rdir + '/' + '.node_map.data'

def show():
    print("--------------show-----------")
    for key,value in node_map.items():
        print("mac: %s, ip: %s" % (key, value.nip))
    print("-----------------------------")
def find_by_ip(ip):
    if ip is None:
        return None
    rt=[]
    for key,value in node_map.items():
        if value.nip == ip:
            rt.append(value)
    return rt
def get_node(mac):
    if node_map.__contains__(mac):
        return node_map[mac]
    return None
def new_node(node):
    if not isinstance(node, Node):
        raise TypeError("[node/new_node]: node is not Node type")
    if node_map.__contains__(node.nid):
        raise ValueError("[node/new_node]: key is exist.")
    node_map[node.nid] = node
def rm_node(node):
    if not isinstance(node, Node):
        raise TypeError("[node/rm_node]: node is not Node type")
    if not node_map.__contains__(node.nid):
        raise ValueError("[node/rm_node]: key do not in map.")
    del node_map[node.nid]
def store():
    f = open(serial_filename, 'wb')
    pickle.dump(node_map, f)
    f.close()
def restore():
    if os.path.exists(serial_filename) is False:
        print("%s is not exist" % serial_filename)
        return
    f = open(serial_filename, 'rb')
    global node_map
    node_map = pickle.load(f)
    f.close()

class Node:
    'define Node members'

    def __init__(self, mac, nip, username, mask=None, hostname=None, describe=None):
        self.nid = mac 
        self.nip = nip
        self.username = username
        self.mask = mask
        self.hostname = hostname
        self.describe = describe 
        self.tags = None
        self.prehost = None
    def show(self):
        rt = "Node detail: ip is %s, mac is %s, hostname is %s \n\
                describe is %s." % (self.nip, self.nid, self.hostname, self.describe)
        return rt
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
        if other is None:
            return False
        if not isinstance(other, Node):
            raise TypeError("[Node/__eq__]: other is not Node type")
        if self.nid == other.nid and self.nip == other.nip:
            return True
        return False

