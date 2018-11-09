"""

https://docs.python.org/3/library/argparse.html
"""

import argparse

parser = argparse.ArgumentParser(description="Probando Command Line arguments")
parser.add_argument("--foo", default=1, type=int, help="Super ayuda")
parser.add_argument("-v", default=5, type=int, help="valor 01")
parser.add_argument("-d", default=6, type=int, help="valor 02")
args = parser.parse_args()
print(args)
print(args.foo)
print(args.v + args.d)