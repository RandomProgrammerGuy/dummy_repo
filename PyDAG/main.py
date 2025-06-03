from graph import graph
from node import node
from edge import edge

my_nodes = [node(0, "A", [edge(0, 1)]), 
            node(1, "B", [edge(1, 2)]), 
            node(2, "C", [edge(2, 3)]),
            node(3, "D", []),
            node(4, "E", [edge(4, 5)]),
            node(5, "F", [edge(5, 1), edge(5, 2)])
            ]

my_graph = graph(my_nodes)

print(my_graph)
## print(my_graph.is_acyclic())
print(my_graph.topological_ordering())