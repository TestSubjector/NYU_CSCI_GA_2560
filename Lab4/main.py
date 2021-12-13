import argparse
import logging
import sys
import os
from file import handle_train_file, handle_test_file, set_nodes
from knn.knn import output_knn, e2, manh

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-train", const=str, nargs="?", default=None)
    parser.add_argument("-test", const=str, nargs="?", default=None)
    parser.add_argument("-k", const=int, type=int, nargs="?", default=3)
    parser.add_argument("-d", const=str, nargs="?", default="e2")
    parser.add_argument("-unitw", type=bool, nargs="?", default=False)
    args = parser.parse_args()

    train_data = handle_train_file(args)
    train_node_list = set_nodes(train_data)

    test_data = handle_test_file(args)
    test_node_list = set_nodes(test_data)

    if args.d == "e2":
        output_knn(train_node_list, test_node_list, args.k, distance_fn=e2, unitw=args.unitw)
    elif args.d == "manh":
        output_knn(train_node_list, test_node_list, args.k, distance_fn=manh, unitw=args.unitw)
    else:
        print("Distance flag has an error. Terminating program")
        exit(0)

if __name__ == "__main__":
    main()
