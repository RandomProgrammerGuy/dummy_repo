from node import node

class graph:
    nodes = []
    node_count = 0
    edges = []


    def __init__(self, nodelist):
        self.nodes = nodelist
        self.node_count = len(nodelist)

        for node in self.nodes:
            for edge in node.edges:
                if edge not in self.edges:
                    self.edges.append(edge)


    def __str__(self):
        returntext = f"Graph {self.__class__.__name__} with nodes:\n"

        for node in self.nodes:
            returntext += f"-- {node}\n"
        
        returntext += "\nand with edges:\n"

        for edge in self.edges:
            returntext += f"-- {edge}\n"

        return returntext
    

    def direct_path_between(self, A : node, B : node):
        """
        Returns a bool indicating whether a direct path exists between two nodes

        Keyowrd arguments:
        A : node -- The origin node
        B : node -- The deestination node
        """
        for edge in self.edges:
            if edge.orig == A:
                if edge.dest == B:
                    return True
                
        return False
    

    def path_between(self, A, B):
        if self.direct_path_between(A, B):
            return True
        
        if A.edge_count() == 0:
            return False
    

    def is_acyclic(self):
        for node in self.nodes:
            if self.path_between(node.id, node.id):
                return True       
        return False
        