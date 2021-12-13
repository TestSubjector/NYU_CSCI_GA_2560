import argparse
import logging
import sys
import os
from file import handle_file, set_nodes, set_centroids
from knn.knn import output_knn, e2, manh, sanity_check
from kmeans.kmeans import sanity_check_kmeans

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-mode", const=str, nargs="?", default="knn")
    parser.add_argument("-data", const=str, nargs="?", default=None)
    parser.add_argument("-centroids", type=str, nargs="+", default=None)
    parser.add_argument("-train", const=str, nargs="?", default=None)
    parser.add_argument("-test", const=str, nargs="?", default=None)
    parser.add_argument("-k", const=int, type=int, nargs="?", default=3)
    parser.add_argument("-d", const=str, nargs="?", default="e2")
    parser.add_argument("-unitw", type=bool, nargs="?", default=False)
    args = parser.parse_args()

    if args.mode == "knn":
        train_data = handle_file(args.train)
        train_node_list = set_nodes(train_data)

        test_data = handle_file(args.test)
        test_node_list = set_nodes(test_data)

        sanity_check(train_node_list, test_node_list)

        if args.d == "e2":
            output_knn(train_node_list, test_node_list, args.k, distance_fn=e2, unitw=args.unitw)
        elif args.d == "manh":
            output_knn(train_node_list, test_node_list, args.k, distance_fn=manh, unitw=args.unitw)
        else:
            print("Distance flag has an error. Terminating program")
            exit(0)
    elif args.mode == "kmeans":
        kmeans_data = handle_file(args.data)
        kmeans_node_list = set_nodes(kmeans_data)
        # for item in kmeans_node_list:
        #     item.print_node()
        centroid_list = set_centroids(args.centroids)
        # for item in centroid_list:
        #     item.print_node()
        sanity_check_kmeans(kmeans_node_list, centroid_list)

if __name__ == "__main__":
    main()
