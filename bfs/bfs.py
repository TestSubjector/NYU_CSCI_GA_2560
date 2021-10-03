from collections import deque

def do_bfs(graph, start, end, verbose):
    # print out what we find
    node_queue = deque()
    node_queue.append((start, [start]))
    visited: dict[str, bool] = {}
    visited[start] = True

    while not len(node_queue) == 0:
        (current_node, path) = node_queue.pop()
        if current_node == end:
            if verbose:
                print("Found Goal ",current_node)
                print("Solution: ", end=" ")
            return show_path(path)
        if verbose:    
            print("Visiting %s via" % current_node, end=" ")
            show_path(path)
            # print(node_queue)
        alphabet_edges = sorted(graph.edges[current_node])
        for next_node in alphabet_edges:
            if next_node not in visited:
                node_queue.appendleft((next_node,[*path,next_node]))
                visited[next_node] = True
    print("No path found to %s" % end)

def show_path(path):
    for idx, node in enumerate(path):
        if idx != 0:
            print("-> ", end = " ")
        print(node, end = " ")
    print() # To flush to next line
    return 0