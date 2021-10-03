class Graph:
    def __init__(self):
        self.nodes: dict[str, (int,int)] = dict()
        self.edges: dict[str,set(str)] = dict()
