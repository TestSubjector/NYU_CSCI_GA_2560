class Node:
    def __init__(self, name):
        self.name = name
        self.isChance = False
        self.isDecision = False
        self.isTerminal = False
        self.reward = 0
        self.edges = []
        self.prob = []
        self.value = 0
        self.cur_policy = name

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
        elif len(self.prob) == 1:
            self.isDecision = True
        elif len(self.edges) == 0:
            self.isTerminal = True    
        sum_check = 0
        if self.isChance == True:
            for prob in self.prob:
                # print(prob, " ", type(prob), " ", prob.replace('.','',1).isdigit())
                sum_check += prob
            if sum_check != 1:
                print("Error: Sum of probabilities is not 1 for chance node ", self.name)
                exit(0)

    def print_node(self):
        print(self.name, self.isChance, self.isDecision, self.isTerminal,
            self.value, self.edges, self.prob, self.cur_policy)