class edge:
    orig = None
    dest = None


    def __init__(self, origin, destination):
        self.orig = origin
        self.dest = destination


    def __str__(self):
        return f"Edge from node with id {self.orig} to node with id {self.dest}"