from node import node

def process_nodes(node_list):
    key_list = node_list.keys()
    for key in key_list:
        target_node = node_list[key]
        target_node.node_type()