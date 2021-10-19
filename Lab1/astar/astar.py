
import math
from heapq import heappush, heappop

def do_astar(graph, start, end, verbose):
    node_queue = []
    heappush(node_queue, (0, start, (start)))
    path_cost = {}
    path_cost[(start)] = 0
    # follwed_path = []
    
    while not len(node_queue) == 0:
        # print(node_queue)
        (_,current_node, follwed_path) = heappop(node_queue)
        if current_node == end:
            if verbose:
                print("Found Goal ", current_node)
            print("Solution: ", end=" ")
            show_path(follwed_path)
            return 0
        if verbose:    
            print("Adding", end = " ")
            show_path(follwed_path)
            
        alphabet_edges = sorted(graph.edges[current_node])
        for next_node in alphabet_edges:
            new_cost = path_cost[follwed_path] + get_heuristic(graph.nodes[current_node], 
                graph.nodes[next_node])
            if next_node not in follwed_path:
                new_path = (*follwed_path, next_node)
            else:
                continue
            if new_path not in path_cost or new_cost < path_cost[new_path]:
                path_cost[new_path] = new_cost
                priority = new_cost + get_heuristic(graph.nodes[next_node], 
                    graph.nodes[end])
                heappush(node_queue,(priority, next_node,new_path))
                if verbose: 
                    show_path_choice(follwed_path, next_node, new_cost, priority - new_cost)
            else:
                if verbose: 
                    show_path_choice(follwed_path, next_node, new_cost, get_heuristic(graph.nodes[next_node], 
                    graph.nodes[end]))
    print("No path found to %s" % end)

def get_heuristic(cur, end):
    return math.sqrt((cur[0]-end[0])**2 + (cur[1]-end[1])**2)

def show_path(path):
    for idx, node in enumerate(path):
        if idx != 0:
            print("-> ", end = " ")
        print(node, end = " ")
    print() # To flush to next line
    return 0

def show_path_choice(path, current_node, new_cost, heuristic):
    if current_node in path:
        return 0
    for idx, node in enumerate(path):
        if idx != 0:
            print("-> ", end = " ")
        print(node, end = " ")
    print("-> ", current_node, end = " ")
    print(" ; g= %.2f " % new_cost, " h= %.2f" % heuristic , " f= %.2f" % (new_cost + heuristic))
    return 0
