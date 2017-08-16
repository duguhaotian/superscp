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

    srcnid = None
    ips = tool.get_ips()
    if len(ips) > 1:
        print("---------------------------------------")
        keys = ips.keys()
        i = 0
        for key in keys:
            print("%d.  %s" % (i, ips[key]))
            i += 1
        print("---------------------------------------")
        select = input("which ip use to scp, select the index: ")
        print("you select ip is : %s" % ips[keys[select]] )
        srcnid = keys[select]
    elif len(ips) < 1:
        print("no ether for scp")
        return
    else:
        srcnid = ips.kes()[0]

    srcnid = tool.get_mac(srcnid)
    print("srcnid: %s" % srcnid)
    srcnode = node.get_node(srcnid)
    if srcnode == None:
        print("current host is not register")
        return

    print("node ip,mac,user: %s, %s, %s" % (srcnode.nip, srcnode.nid, srcnode.username))

'''
    tnodes = node.find_by_ip(tip)
    for tnode in tnodes:
        paths.search_by_target(srcnode, tnodes)
    paths.generate("testxxxx")
'''
