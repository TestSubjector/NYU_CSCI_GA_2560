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

def handle_train_file(args):
    try:
        input_file = open(args.train or "input.txt", "r")
    except FileNotFoundError:
        print("Training file not found. Terminating program")
        exit(0)

    input_data = input_file.read()
    input_file.close()
    return input_data

def handle_test_file(args):
    try:
        input_file = open(args.test)
    except FileNotFoundError:
        print("Test file not found. Terminating program")
        exit(0)

    input_data = input_file.read()
    input_file.close()
    return input_data