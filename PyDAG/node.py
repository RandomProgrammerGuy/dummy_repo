from edge import edge

class node:
    id = None
    value = None
    edges = []


    def __init__(self, new_id, val, edge_list):
        self.id = new_id
        self.value = val

        for edge in edge_list:
            if edge.orig == self.id:
                self.edges.append(edge)   
            else:
                raise ValueError(f"{edge} in edges list does not originate from the node {self.value}")
            
    
    def __str__(self):
        returntext = f"Node ID: {self.id}, value: {self.value}. edges:\n"
        
        for edge in self.edges:
            returntext += f"{edge}\n"

        return returntext
    

    def edge_count(self):
        """Returns the number of edges that originate from a node"""
        return len(self.edges)