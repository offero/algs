# Topological Sort

Applies to a Directed Acyclic Graph (DAG).

Whenever we have an edge from x to y, the order visits x before y.

DFS with post-order node additions gives a topological sort.

Redraw DAG so all edges point upwards. Return the order of the nodes.

        OOO
    +-->OOO<-+
    |    ^   |
    |    |   |
    |   OOO--+
    |   OOO
    |    ^
    |    |
    |   OOO
    |   OOO<-+
    |    ^   |
    |    |   |
    |   OOO--+
    |   OOO<-+
    |    ^   |
    |    |   |
    +---OOO--+
        OOO

This ordering forms the basis for other search algorithms because
we know that we will always process the predecessor of x before x.
