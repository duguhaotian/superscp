#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys
import superscp_tool 
import node_data_manager 
from pathmanager import node 
from pathmanager import paths 

def usage(argv):
    show="usage:\n\
            insertLinks {fname}: read link data from fname file and insert into system\n\
            superscp {source_file/dir}  {target_ip}  {target_dir}: scp file or dir to target host\n\
            "
    print(show)

if __name__ == '__main__':
    node.restore()
    node.show()
    paths.restore()
    cmds = {
            'insertLinks': node_data_manager.insert_data,
            'superscp': superscp_tool.superscp
    }
    
    if len(sys.argv) < 2:
        usage(None)
        exit(-1)
    cmds.get(sys.argv[1], usage)(sys.argv)

