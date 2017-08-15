#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
from pathmanager import node 
from pathmanager import link 
from pathmanager import paths 
from pathmanager import tool 

def superscp(argv):
    if len(argv) != 5:
        usage()
        return
    src = argv[2]
    tip = argv[3]
    tdir = argv[4]
    print("source: %s, targetip: %s, targetdir: %s" % (src, tip, tdir))

    tnodes = node.find_by_ip(tip)
    ips = tool.get_ips()
    for key,value in ips.items():
        print("key: %s --- ip: %s" % (key, value))
        mac = tool.get_mac(key)
        srcnode = node.get_node(mac)
        if srcnode == None:
            continue
        for tnode in tnodes:
            paths.search_by_target(srcnode, tnodes)
        paths.generate("testxxxx")

