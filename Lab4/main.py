import argparse
import logging
import sys
import os
from file import handle_file, set_nodes

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", const=str, nargs="?", default=None)
    args = parser.parse_args()

    input_data = handle_file(args)
    node_list = set_nodes(input_data)

if __name__ == "__main__":
    main()
