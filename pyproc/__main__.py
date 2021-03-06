#!/usr/bin/python

import sys
import argparse

try:
    import pyproc
except ImportError:
    sys.path.append('.')
    import pyproc

def main(args):

    path, _, extension = args.file.rpartition('.')

    output_file = '%s_proc.py' % path
    with open(args.file) as inf:
        contents = inf.read()

    with open(output_file, 'w') as inf:
        proc = pyproc.Preprocessor(contents, input_file=args.file, output_file=inf)
        proc.process()

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file', help='The source file to parse.')
    parser.add_argument('-o', metavar='output_file', dest='output_file', default=None)
    main(parser.parse_args())
