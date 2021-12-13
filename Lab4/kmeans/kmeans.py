

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