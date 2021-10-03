from collections import deque

def do_ids(graph, start, end, depth, verbose):
    goal = False
    while not goal:
        visited = {}
        visited[start] = True
        goal = ids_step(graph, visited, [start], end, depth, verbose, depth)
        depth = depth + 1
        if depth >= len(graph.nodes):
            print("Path to goal not found")
            return 0

def ids_step(graph, visited, path, end, depth, verbose, final_depth):
    current_node = path[-1]
    if current_node == end:
        print("Solution: ", end=" ")
        return show_path(path)
    if depth <=0:
        if verbose:
            print("Hit Depth = ",final_depth,": ",current_node)
        return False
    if verbose:
        print("Expand: ", current_node)
    alphabet_edges = sorted(graph.edges[current_node])
    for next_node in alphabet_edges:
        if next_node not in visited:
            visited[next_node] = True
            goal = ids_step(graph, visited, [*path, next_node], end, depth - 1, verbose,final_depth)
            if goal:
                return goal
            
    return False


def show_path(path):
    for idx, node in enumerate(path):
        if idx != 0:
            print("-> ", end = " ")
        print(node, end = " ")
    print() # To flush to next line
    return True