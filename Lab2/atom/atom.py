class Atom:
    def __init__(self):
        self.members = set()

class Binary:
    def __init__(self, token1, op, token2):
        self.left = token1
        self.op = op
        self.right = token2