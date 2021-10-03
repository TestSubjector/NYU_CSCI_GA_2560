import argparse
import logging
import sys
import os
from file import set_graph
from bfs import bfs
from astar import astar
from ids import ids

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler())

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-start", const=str, nargs="?", required=True)
    parser.add_argument("-goal","-end", const=str, nargs="?", required=True)
    parser.add_argument("-alg",const=str, nargs="?", required=True)
    parser.add_argument("-depth",const=str, nargs="?")
    parser.add_argument("-v", const=str, nargs="?")
    parser.add_argument("-i", "--input", const=str, nargs="?")
    args = parser.parse_args()

    # log.warning("Loading Data")

    try:
        graph_file = open(args.input or "input.txt", "r")
    except FileNotFoundError:
        print("File input.txt not found. Terminating program")
        exit(0)
    graph_data = graph_file.read()
    graph_file.close()

    input_graph = set_graph(graph_data)

    verbose = False
    if args.v != None:
        verbose = True

    decide_alg = args.alg.upper() 
    if decide_alg == "BFS":
        bfs.do_bfs(input_graph, args.start, args.goal, verbose)
    elif decide_alg == "ASTAR":
        astar.do_astar(input_graph, args.start, args.goal, verbose)
    elif decide_alg == "IDS":
        if args.depth == None:
            print("Depth not given for IDS. Terminating program.")
            exit(0)
        ids.do_ids(input_graph, args.start, args.goal, int(args.depth), verbose)
    else:
        print("Algorithm name given to the flag is incorrect. Terminating program")
            
if __name__ == "__main__":
    main()
