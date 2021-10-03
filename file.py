from graph import graph

def set_graph(graph_data):
    input_graph = graph.Graph()
    splitdata = graph_data.split("\n")
    for _, line in enumerate(splitdata):
        line = line.strip().split()
        if (not line) or (line[0][0] == "#"):
            continue
        elif (len(line) == 3) and (line[1].isnumeric() == True and line[2].isnumeric() == True):
            input_graph.nodes[line[0]] = (int(line[1]), int(line[2]))
        elif (len(line) == 2):
            if line[0] in input_graph.edges:
                # print(input_graph.edges)
                input_graph.edges[line[0]].add(line[1])
            else:
                input_graph.edges[line[0]]= {line[1]}

            if line[1] in input_graph.edges:
                # print(input_graph.edges)
                input_graph.edges[line[1]].add(line[0])
            else:
                input_graph.edges[line[1]]= {line[0]}
        else:
            log.error("Input File has invalid format: Not a comment, vertex or an edge. Terminating program")
            exit(0)
    return input_graph
