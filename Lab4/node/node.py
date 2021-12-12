class Node:
    def __init__(self, identity):
        self.pred_list = []
        self.identity = identity

    def add_pred(self, pred):
        self.pred_list.append(pred)

    def print_node(self):
        print(self.identity, self.pred_list)
