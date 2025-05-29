from graph import graph
from node import node
from edge import edge

my_nodes = [node(0, "A", [edge(0, 1)]), 
            node(1, "B", [edge(1, 2)]), 
            node(2, "C", [edge(2, 3)]),
            node(3, "D", [edge(3, 4)]),
            node(4, "E", [edge(4, 2)])]

my_graph = graph(my_nodes)

print(my_graph)
print(my_graph.is_acyclic())