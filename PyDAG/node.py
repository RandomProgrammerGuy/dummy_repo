from connection import connection

class node:
    id = None
    value = None
    connections = []


    def __init__(self, new_id, val, conns):
        self.id = new_id
        self.value = val

        for connection in conns:
            if connection.orig == self.id:
                self.connections.append(connection)   
            else:
                raise ValueError(f"{connection} in connections list does not originate from the node {self.value}")
            
    
    def __str__(self):
        returntext = f"Node ID: {self.id}, value: {self.value}. connections:\n"
        
        for conn in self.connections:
            returntext += f"{conn}\n"

        return returntext