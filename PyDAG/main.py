from graph import graph
from node import node
from connection import connection

my_nodes = [node(0, "A", [connection(0, 1), connection(0, 3)]), 
            node(1, "B", [connection(1, 2), connection(1, 4)]), 
            node(2, "C", [connection(2, 3)]),
            node(3, "D", [connection(3, 4)]),
            node(4, "E", [])]

my_graph = graph(my_nodes)

print(my_graph)
print(my_graph.path_between(0, 0))