# Topological Sort

Applies to a Directed Acyclic Graph (DAG).

Whenever we have an edge from x to y, the order visits x before y.

Redraw DAG so all edges point upwards. Return the order of the nodes.

From:

┌────┐  5   ┌───┐  5   ┌───┐  1   ┌───┐
│ 1  │ ───> │ 2 │ ───> │ 4 │ ───> │ 6 │
└────┘      └───┘      └───┘      └───┘
  │                      ∧
  │ 1                    │
  ∨                      │
┌────┐  1                │
│ 3  │ ──────────────────┘
└────┘
  │
  │ 1
  ∨
┌────┐
│ 5  │
└────┘

To:

      ┌────┐
      │ 6  │ <┐
      └────┘  │
      ┌────┐  │
  ┌─> │ 5  │  │ 1
  │   └────┘  │
  │           │
  │     ┌─────┘
  │     │
  │   ┌────┐
  │ 1 │ 4  │
  │   └────┘
  │     ∧
  │     │ 1
  │     │
  │   ┌────┐
  └── │ 3  │ <┐
      └────┘  │
      ┌────┐  │
      │ 2  │  │
      └────┘  │
        ∧     │ 1
        │ 5   │
        │     │
      ┌────┐  │
      │ 1  │ ─┘
      └────┘


This ordering forms the basis for other search algorithms because
we know that we will always process the predecessor of x before x.

## Algorithm 1:

DFS with post-order node additions gives a topological sort.

## Algorithm 2:

Find a node with 0 in-degree. Add it to the topo list. Remove it from the
graph. Repeat until 0 nodes in graph.

### Cycle Detection

We can use this algorithm to detect cycles. If we go through n distinct nodes
without finding one with 0 in-degree, then the graph contains a cycle.
While building a predecessor chain, if we see a node in the chain that we have
already visited, then there is a cycle.


# Misc.

Graphs made using Graph::Easy
