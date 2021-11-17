from node import node  

def set_nodes(graph_data):
    node_list = {}
    splitdata = graph_data.split("\n")
    for idx, line in enumerate(splitdata):
        line = line.replace("=", " = ")
        line = line.replace(":", " : ")
        line = line.replace("%", " % ")
        line = line.replace("[", " [ ")
        line = line.replace("]", " ] ")
        line = line.replace(",", " ")
        line = line.strip().split()
        if (not line) or (line[0][0] == "#"):
            continue

        line = [float(item) if item.replace('.','',1).isdigit() == True else item for item in line]    

        check_new_node(line[0], node_list)
        new_node = node_list[line[0]]
        if line[1] == "=":
            new_node.reward = float(line[2])
        elif line[1] == "%":
            for prob_value in line[2:]:
                new_node.add_prob(prob_value)
        elif line[1] == ":":
            for node_name in line[3:-1]:
                check_new_node(node_name, node_list)
                new_node.add_edge(node_name)
        else:
            print(line[1]," is non [:,%,=] format")
        # new_node.print_node()
    return node_list

def check_new_node(node_name, node_list):
    if node_name not in node_list:
        new_node = node.Node(node_name)
        node_list[new_node.name] = new_node
    return node_list

def handle_file(args):
    try:
        input_file = open(args.input or "input.txt", "r")
    except FileNotFoundError:
        print("File input.txt not found. Terminating program")
        exit(0)

    input_data = input_file.read()
    input_file.close()
    return input_data