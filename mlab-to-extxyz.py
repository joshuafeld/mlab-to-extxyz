#!/usr/bin/env python3

import sys
import os

from parser import parse_mlab
from writer import write_extxyz

def convert(input_path: str, output_path: str) -> None:
    """Converts from ML AB to extended XYZ file format.

    Parameters
    ----------
    input_path: str
        The path of the input file.
    output_path: str
        The path of the output file.
    """

    write_extxyz(parse_mlab(input_path), output_path)

def main() -> None:
    # Set the input file path from the first command line argument if provided or use the default
    # value (ML_AB) and check if the file exists.
    input_path = 'ML_AB'
    if len(sys.argv) >= 2:
        input_path = os.path.abspath(sys.argv[1])
    if not os.path.exists(input_path):
        print('The input file does not exist.')
        return

    # Set the output file path from the second command line argument if provided or use the default
    # value (output.extxyz).
    output_path = 'output.extxyz'
    if len(sys.argv) >= 3:
        output_path = os.path.abspath(sys.argv[2])

    # Convert from ML AB to extended XYZ.
    convert(input_path, output_path)

if __name__ == "__main__":
    main()