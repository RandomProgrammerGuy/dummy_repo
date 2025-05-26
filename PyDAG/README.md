# PyDAG

A Python implementation of Directed Acyclic Graphs (DAGs). 

## Implementation

The `graph` class contains a list of `node` objects, as well as the number of its nodes, stored in the `node_count` attribute. It also includes a `connections` attribute which is a list of all the different connections in the graph. Note that a `graph` object in this implementation is not necessarily cyclic.

The `node` class contains a `value` attribute and a `connections` attribute. The `connections` attribute only includes connections that **originate** from the node in question. The `connections` attribute in a `graph` object is constructed from the `connections` attributes in each node.

The `connection` class contains an `origin` and a `destination` attribute. 

## Methods

The `graph` class contains the following methods:

- `.is_cyclic()` : returns a `bool` indicating if a graph is cyclic
- `.transitive_closure()` : returns the transitive closure of the graph if it is a DAG, while not modifying the original graph
- `.transitive_reduction()` : returns the transitive reduction of the graph if it is a DAG, while not modifying the original graph
- `.topological_ordering()` : returns the topological ordering of the graph if it is a DAG, while not modifying the original graph

The `node` class contains the following methods :

- `.reachable_from(A)` : returns a `bool` indicating if the node it is called on is reachable from the node A
- `.can_reach(A)` : returns a `bool` indicating if the node A is reachable fromm the node it is called on