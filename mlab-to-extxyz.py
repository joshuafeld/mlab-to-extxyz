#!/usr/bin/env python3

import sys
import os

from parser import parse_mlab
from writer import write_extxyz

def main():
    input_path = 'ML_AB'
    if len(sys.argv) >= 2:
        input_path = os.path.abspath(sys.argv[1])
        if not os.path.exists(input_path):
            print('the input file you provided does not exist or the path to it is wrong')
            return

    output_path = 'output.extxyz'
    if len(sys.argv) >= 3:
        output_path = os.path.abspath(sys.argv[2])

    write_extxyz(parse_mlab(input_path), output_path)

main()