#!/usr/bin/env python3

import sys
import os

from ml_ab_parser import convert

def main():
	output_file = 'output.extxyz'
	
	if len(sys.argv) == 1:
		print('you have to provide the path to the input file')
		return 0
	
	if len(sys.argv) >= 4:
		print('too many arguments')
		return

	input_file = os.path.abspath(sys.argv[1])

	if not os.path.exists(input_file):
		print('the input file you provided does not exist or the path to it is wrong')
		return
	
	if len(sys.argv) == 3:
		output_file = sys.argv[2]

	convert(input_file, output_file)

main()