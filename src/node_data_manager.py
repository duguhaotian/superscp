#!/usr/bin/python
# -*- coding: UTF-8 -*-

from main import usage
from pathmanager import node 
from pathmanager import link 
from pathmanager import paths 

def insert_data(argv):
    if len(argv) != 3:
        usage()
        return
    print
    fname = argv[2]
    f = open(fname, 'rb')
    flag = False
    path = None 
    for line in f:
        line = line.strip('\n')
        line = line.strip()
        if line.startswith('name:'):
            flag = True
            lname = line[5:len(line)]
            lname = lname.strip()
            path = link.Link(lname)
            continue
        if path == None:
            continue
        strs = line.split(',')
        if len(strs) != 6:
            print("invalid data line: %s" % line)
            continue
        tnode = node.Node(strs[0], strs[1], strs[2], strs[3], strs[4], strs[5]) 
        node.new_node(tnode)
        path.insert(tnode)

    print(path.show())
    paths.insert(path)
    paths.store()
    node.store()

