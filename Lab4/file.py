from node import node  

def set_nodes(graph_data):
    node_list = []
    splitdata = graph_data.split("\n")
    for idx, line in enumerate(splitdata):
        line = line.replace(",", " ")
        line = line.strip().split()
        if (not line) or (line[0][0] == "#"):
            continue
        
        current_node = node.Node(line[-1])
        for pred in line[:-1]:
            current_node.add_pred(int(pred))
        # current_node.print_node()
        node_list.append(current_node)
    return node_list

def handle_file(args_input):
    try:
        input_file = open(args_input, "r")
    except FileNotFoundError:
        print("Training file not found. Terminating program")
        exit(0)

    input_data = input_file.read()
    input_file.close()
    return input_data

def set_centroids(centroid_args):
    centroid_list = []
    for idx,item in enumerate(centroid_args):
        item = item.replace(","," ").strip().split()
        current_node = node.Node("C"+str(idx+1))
        for coord in item:
            current_node.add_pred(int(coord))
        centroid_list.append(current_node)
    return centroid_list