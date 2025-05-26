from connection import connection

class node:
    value = None
    connections = []


    def __init__(self, val, conns):
        self.value = val

        for connection in conns:
            if connection.orig == self.value:
                self.connections.append(connection)   
            else:
                raise ValueError(f"{connection} in connections list does not originate from the node {self.value}")
            
    
    def __str__(self):
        returntext = f"Node {self.value} with connections:\n"
        
        for conn in self.connections:
            returntext += f"{conn}\n"

        return returntext