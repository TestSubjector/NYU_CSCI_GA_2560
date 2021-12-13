import operator

def output_knn(train_list, test_node_list, k_value, distance_fn, unitw):
    output_process = {} # Tuple for (Match, Want, Got)
    for test_node in test_node_list:
        do_knn(train_list, test_node, k_value, distance_fn, unitw, output_process)
    for label_key in output_process:
        match = str(output_process[label_key][0])
        got = str(output_process[label_key][1])
        want = str(output_process[label_key][2])
        print("Label="+ label_key + " Precision=" + match + "/" + got + 
            " Recall=" + match + "/" + want)

def do_knn(train_list, test_node, k_value, distance_fn, unitw, output_process):
    distance_store = []
    for index, train_node in enumerate(train_list):
        distance = distance_fn(train_node, test_node)
        distance_store.append((index, distance))
    
    distance_store.sort(key=on_index)
    selected_distances = distance_store[:k_value]
    vote_dict = {}
    for _, item in enumerate(selected_distances):
        index = item[0]
        node_label = train_list[index].identity
        weight = 1/(max(item[1], 0.0001))
        if unitw != False:
            weight = 1
        if node_label in vote_dict:
            vote_dict[node_label] += weight
        else:
            vote_dict[node_label] = weight
    got_identity = max(vote_dict.items(), key=operator.itemgetter(1))[0]
    print("want=" + test_node.identity + " got=" + got_identity)
    if test_node.identity not in output_process:
        output_process[test_node.identity] = [0,0,0]
    output_process[test_node.identity][0] += int(test_node.identity == got_identity)
    output_process[test_node.identity][2] += 1 
    if got_identity not in output_process:
        output_process[got_identity] = [0,0,0]
    output_process[got_identity][1] += 1

def e2(node1, node2):
    total_sum = 0
    for idx, pred in enumerate(node1.pred_list):
        total_sum += (pred - node2.pred_list[idx])**2
    return total_sum

def manh(node1, node2):
    return sum(abs(e1-e2) for e1, e2 in zip(node1.pred_list,node2.pred_list))

def on_index(element):
    return element[1]

def sanity_check(train_list, test_list):
    dimension = len(train_list[0].pred_list)
    for idx, node in enumerate(train_list):
        if len(node.pred_list) != dimension:
            print("Dimension problems for training input, number -", idx,". Terminating program")
            exit(0)
    for idx, node in enumerate(test_list):
        if len(node.pred_list) != dimension:
            print("Dimension problems for testing input, number -", idx,". Terminating program")
            exit(0)