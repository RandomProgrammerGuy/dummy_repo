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
    

    def direct_path_between(self, A : int, B : int):
        """
        Returns a bool indicating whether a direct path exists between two nodes of
        a graph

        Keyowrd arguments:
        A : int -- The id of the origin node
        B : int -- The id of the deestination node
        """
        for edge in self.edges:
            if edge.orig == A:
                if edge.dest == B:
                    return True
                
        return False
    

    def direct_edges_of(self, A : int):
        """
        Returns a list of the nodes directly accessible from a node

        Keyword arguments:
        A : int -- the id of the origin node
        """
        nodes_list = []

        for edge in self.edges:
            if edge.orig == A:
                nodes_list.append(edge.dest)

        return nodes_list

    def path_between(self, A : int, B : int): # INCOMPLETE
        """
        Returns a bool indicating whether a path (direct or indirect) exists between
        two nodes of a graph

        Keyowrd arguments:
        A : int -- The id of the origin node
        B : int -- The id of the deestination node
        """

        if self.direct_path_between(A, B):
            return True
        
        if A.edge_count() == 0:
            return False
        
        nodes_visited = []

        nodes_visited += self.direct_edges_of(A)

        while len(nodes_visited) <= self.node_count:
            for node in nodes_visited:
                current_node_edges = self.direct_edges_of(node)

                for dest in current_node_edges:
                    if dest not in nodes_visited:
                        nodes_visited.append(dest)

                if B in nodes_visited:
                    return True
                
        return False

    

    def is_acyclic(self):
        """Returns a bool indicating whether a graph is acyclic."""
        for node in self.nodes:
            if self.path_between(node.id, node.id):
                return True       
        return False
    

    def in_degree_of(self, A : int):
        """Returns the in-degree of the node with an ID of A
        
        Keyword arguments:
        A : int -- The id of the node
        """
        counter = 0

        for edge in self.edges:
            if edge.dest == A:
                counter += 1

        return counter

        
    
    def topological_ordering(self):
        """
        Returns a topological ordering of the graph
        """
        queue = []
        topological_ordering = []

        for node in self.nodes:
            if self.in_degree_of(node.id) == 0:
                queue.append(node.id)

        while len(queue) != 0:
            current_elem = queue.pop(0)
            topological_ordering.append(current_elem)

            for i in range(len(self.edges)):
                if self.edges[i].orig == current_elem:
                    removed_edge = self.edges.pop(i)

                    if self.in_degree_of(removed_edge.dest) == 0:
                        if removed_edge.dest not in queue:
                            queue.append(removed_edge.dest)

                if i+1 >= len(self.edges):
                    break

        return topological_ordering