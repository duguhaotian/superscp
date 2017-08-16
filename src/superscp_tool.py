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

    print(srcnode.show())

    tnodes = node.find_by_ip(tip)
    tnode = None
    if len(tnodes) > 1:
        i = 0
        print("***********************************")
        for tmp in tnodes:
            print("%d. %s" % (i, tmp.show()))
            i += 1
        print("***********************************")
        select = input("which target ip use to scp, select the index: ")
        tnode = tnodes[select]
    elif len(tnodes) < 1:
        print("can not find target node by target ip : %s" % tip)
        return
    else:
        tnode = tnodes[0]
    
    #idxs = paths.search_by_target(srcnode, tnode)
    #paths.generate("testxxxx")

