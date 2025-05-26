class connection:
    orig = None
    dest = None


    def __init__(self, origin, destination):
        self.orig = origin
        self.dest = destination


    def __str__(self):
        return f"Connection from node {self.orig} to node {self.dest}"