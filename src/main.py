#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
from pathmanager import node 
from pathmanager import link 
from pathmanager import paths 

def usage():
    show="usage:\n\
            insertLinks {fname}: read link data from fname file and insert into system\n\
            superscp {source_file/dir}  {target_ip}  {target_dir}: scp file or dir to target host\n\
            "
    print(show)

def insert_data():
    if len(sys.argv) != 3:
        usage()
        return
    print
    fname = sys.argv[2]
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

    path.show()
    paths.insert(path)
    paths.store()
    node.store()

def superscp():
    if len(sys.argv) != 5:
        usage()
        return
    print("source: %s, targetip: %s, targetdir: %s" % (sys.argv[2], sys.argv[3], sys.argv[4]))


if __name__ == '__main__':
    cmds = {
            'insertLinks': insert_data,
            'superscp': superscp
    }
    
    cmds.get(sys.argv[1], usage)()

