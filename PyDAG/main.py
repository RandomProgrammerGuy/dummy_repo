from graph import graph
from node import node
from connection import connection

my_nodes = [node(1, [connection(1,2)]), node(2, [connection(2,3)]), node(3, [])]

my_graph = graph(my_nodes)

print(my_graph)