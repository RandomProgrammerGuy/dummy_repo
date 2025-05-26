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
                self.connections.append(connection)


    def __str__(self):
        returntext = f"Graph {self.__class__.__name__} with nodes:\n"

        for node in self.nodes:
            returntext += f"-- {node}\n"
        
        returntext += "\nand with connections:\n"

        for connection in self.connections:
            returntext += f"-- {connection}\n"

        return returntext