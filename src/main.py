#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
from pathmanager import node 
from pathmanager import link 
from pathmanager import paths 

def usage():
    show="usage:\n\
            newnode: create node store host information\n\
            "
    print(show)
if __name__ == '__main__':
    usage()
    tdir=os.path.split(os.path.realpath(__file__))[0]
    print(tdir)
    paths.restore()
    tmp=paths.lstore.get(0)
    tmp.show()

