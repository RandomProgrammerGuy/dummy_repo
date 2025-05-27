from node import node

class graph:
    nodes = []
    node_count = 0
    connections = []


    def __init__(self, nodelist):
        self.nodes = nodelist
        self.node_count = len(nodelist)

        for node in self.nodes:
            for connection in node.connections:
                if connection not in self.connections:
                    self.connections.append(connection)


    def __str__(self):
        returntext = f"Graph {self.__class__.__name__} with nodes:\n"

        for node in self.nodes:
            returntext += f"-- {node}\n"
        
        returntext += "\nand with connections:\n"

        for connection in self.connections:
            returntext += f"-- {connection}\n"

        return returntext
    

    def direct_path_between(self, A, B):
        for connection in self.connections:
            if connection.orig != A:
                pass
            else:
                if connection.dest == B:
                    return True
                
        return False
    

    def path_between(self, A, B):
        if self.direct_path_between(A, B):
            return True
        
        nodes_visited = []
        direct_nodes = []

        for node in self.nodes:
            if self.direct_path_between(A, node.id):
                direct_nodes.append(node.id)
                nodes_visited.append(node)

        if direct_nodes == []:
            return False

        for node in direct_nodes:
            if self.path_between(node, B) :
                return True
            
        return False