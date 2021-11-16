import argparse
import logging
import sys
import os
from file import handle_file, set_nodes
from process import process

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-df", const=str, nargs="?", default=1.0)
    parser.add_argument("-min", const=str, nargs="?", default= False)
    parser.add_argument("-tol",const=str, nargs="?", default=0.01)
    parser.add_argument("-iter",const=str, nargs="?", default=100)
    parser.add_argument("-i", "--input", const=str, nargs="?", default=None)
    args = parser.parse_args()

    # args.mode = args.mode.upper()

    input_data = handle_file(args)
    node_list = set_nodes(input_data)
    process.process_nodes(node_list)
    for key in node_list.keys():
        node_list[key].print_node()

if __name__ == "__main__":
    main()
