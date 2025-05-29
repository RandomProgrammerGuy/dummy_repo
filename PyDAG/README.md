# PyDAG

A Python implementation of Directed Acyclic Graphs (DAGs). 

## Implementation

The `graph` class contains a list of `node` objects, as well as the number of its nodes, stored in the `node_count` attribute. It also includes a `edges` attribute which is a list of all the different edges in the graph. Note that a `graph` object in this implementation is not necessarily cyclic.

The `node` class contains an `id` attribute, a `value` attribute and a `edges` attribute. The `edges` attribute only includes edges that **originate** from the node in question. The `edges` attribute in a `graph` object is constructed from the `edges` attributes in each node. The `id` attribute is used to identify nodes in the graph.

The `edge` class contains an `origin` and a `destination` attribute. 

## Methods

The `graph` class contains the following methods:

- `.is_acyclic()` : returns a `bool` indicating if a graph is acyclic
- `.transitive_closure()` : returns the transitive closure of the graph if it is a DAG, while not modifying the original graph
- `.transitive_reduction()` : returns the transitive reduction of the graph if it is a DAG, while not modifying the original graph
- `.topological_ordering()` : returns the topological ordering of the graph if it is a DAG, while not modifying the original graph
- `.direct_path_between(A, B)` : returns a `bool` indicating if there is a direct path between nodes A and B. (A and B are IDs)
- `.path_between(A, B)` : returns a `bool` indicating if there is a direct or indirect path between nodes A and B. (A and B are IDs)