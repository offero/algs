# Topological Sort

Applies to a Directed Acyclic Graph (DAG).
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
