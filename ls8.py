"""Main."""

import sys
from cpu import *

cpu = CPU()

if len(sys.argv) < 2:
    print('please specify the program to run!')
else:
    cpu.load()
    cpu.run() 
