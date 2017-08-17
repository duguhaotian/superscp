#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import subprocess
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
        srcnid = ips.keys()[0]

    srcnid = tool.get_mac(srcnid)
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

    print(tnode.show())
    
    idxs = paths.search_by_target(srcnode, tnode)
    path = None
    if len(idxs) > 1:
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        i = 0
        for idx in idxs:
            print("%d. %s" % (i, paths.get(idx).show()))
            i += 1
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        select = input("select one path to scp, which index you chose: ")
        path = paths.get(idxs[i])
    elif len(idxs) < 1:
        print("cannot find sourceip: %s to targetip: %s path" % (srcnode.nip, tnode.nip))
        return
    else:
        path = paths.get(idxs[0])

    rdir=os.path.split(os.path.realpath(__file__))[0]
    scpfname = rdir + "/scptool/.data.superscp"
    paths.generate_scp_data(path, scpfname)

    cmdstr = rdir+"/scptool/magic.sh " + src + " " + tdir 
    rts = subprocess.check_output(cmdstr, shell=True).decode().strip()
    print("magic return: %s", rts)

