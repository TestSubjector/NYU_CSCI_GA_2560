from operator import add

def run_kmeans(data_list, centroid_list, distance_fn):
    k_value = len(centroid_list)
    max_iter = 1000 # Prevent infinite loop
    while True:
        categories = {}

        for i in range(k_value):
            categories[i] = []

        for node in data_list:
            distances = [(idx,distance_fn(node, centroid)) for idx,centroid in enumerate(centroid_list)]
            distances.sort(key=on_index)
            closest_centroid = distances[0][0]
            categories[closest_centroid].append(node)

        exit_flag = True

        for i in range(k_value):
            if len(categories[i]) == 0:
                continue
            cur_centroid = centroid_list[i]
            dimension = len(cur_centroid.pred_list)
            new_centroid = [0] * dimension
            for node in categories[i]:
                new_centroid = list(map(add,new_centroid,node.pred_list))
            new_centroid = [element/len(categories[i]) for element in new_centroid]
            diff = [abs(cur_centroid.pred_list[idx] - new_centroid[idx]) for idx in range(dimension)]
            if sum(diff) > 0.00001:
                exit_flag = False
                centroid_list[i].pred_list = new_centroid
        if exit_flag:
            for i in range(k_value):
                print(centroid_list[i].identity,"= {",end="")
                for node in categories[i]:
                    if node == categories[i][-1]:
                        print(node.identity,end="")
                    else:
                        print(node.identity+",",end="")
                print("}")
            for i in range(k_value):
                print("(", end="")
                print(centroid_list[i].pred_list, end="")
                print(")")
            break
    
def e2(node1, node2):
    total_sum = 0
    for idx, pred in enumerate(node1.pred_list):
        total_sum += (pred - node2.pred_list[idx])**2
    return total_sum

def manh(node1, node2):
    return sum(abs(e1-e2) for e1, e2 in zip(node1.pred_list,node2.pred_list))

def sanity_check_kmeans(kmeans_list, centroid_list):
    dimension = len(kmeans_list[0].pred_list)
    for idx, node in enumerate(kmeans_list):
        if len(node.pred_list) != dimension:
            print("Dimension problems for kmeans data input, number -", idx,". Terminating program")
            exit(0)
    for idx, node in enumerate(centroid_list):
        if len(node.pred_list) != dimension:
            print("Dimension problems for centroid input, number -", idx,". Terminating program")
            exit(0)
    
def on_index(element):
    return element[1]