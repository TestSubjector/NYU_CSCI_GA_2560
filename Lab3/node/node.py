class Node:
    def __init__(self, name):
        self.name = name
        self.isChance = False
        self.isDecision = False
        self.isTerminal = False
        self.reward = 0
        self.edges = []
        self.prob = []

    def add_edge(self, edge):
        self.edges.append(edge)

    def add_prob(self, prob_value):
        self.prob.append(prob_value) 

    def node_type(self):
        if len(self.edges) > 0 and len(self.edges) == len(self.prob):
            self.isChance = True
        elif len(self.prob) == 1:
            self.isDecision = True
        elif len(self.edges) > 0 and len(self.prob) == 0:
            self.isDecision = True
            self.add_prob(1)
        elif len(self.edges) == 0:
            self.isTerminal = True    

    def print_node(self):
        print(self.name, self.isChance, self.isDecision, self.isTerminal,
            self.reward, self.edges, self.prob)