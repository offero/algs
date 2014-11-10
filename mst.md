# Minimum Spanning Trees

Graph Cut: A partitioning of a graph into 2 components.

Cut property: The minimum weight crossing edges of a cut is in the MST.

General algorithm:

- Color all adges grey.
- Find a cut with no black\* crossing edges
- Color the minimum crossing edge black
- Repeat until N-1 black edges

\*Black edges are in the MST.

## Kruskal's algorithm

- Sort the edges by weight
- Add the minimum edge to the MST unless it would create a cycle (throw away if
  so)
- Repeat until N-1 edges in the MST.

## Prim's algorithm

Greedy algorithm (like Dijkstra)

Use a Priority Queue to maintain the frontier edges. When a new edge is added
to the MST, add the new node's edges to the PQ.
Add minimum frontier edge to MST if it would not create a cycle (both ends
already on the MST).

The Priority Queue contains edges that are connected to the tree. New edges
are added to the PQ as the tree grows.

### Optimization

Augment the Priority Queue such that we can modify the minimum cost edge from
a *Node* on the frontier. This results in less memory use the PQ; at most
1 edge per node O(N) PQ size. This also requires us to add a data structure
to the priority queue that can index into the PQ by Node ID (The PQ is
sorted by edge weight).

## Cycle detection

Use a data structure that can keep track of connected components and component
membership to perfom cycle detection. A cycle occurs whenever an edge is added
between 2 nodes that are in the same connected component
(IE. already a part of the tree).

Use a UnionFind data structure to perform cycle detection.

## UnionFind

UnionFind implements 2 primary operations:

- union(a, b) -> Component ID : Join the components that contain objects a and b.
- connected(a, b) -> Boolean  : Is a and b in the same component?

### Naive Implementation

Initialize each node as belonging to its own component.
union(a, b) changes b's component to a's. It also changes all of the components
that are in b's component to a's. O(N).
connected(a, b) simply checks that the components of both a and b are the same
O(1).

### Quick Union

Technique: Use a tree to represent a component.
A component is a tree with a root node. Each node belongs to a tree. Each node
keeps reference to its parent. The top most parent is the root.

Implement a findRoot operation.

- findRoot(a) -> root/component: Given a Node ID a, find the root of the tree
    (component) to which a belongs.

Keep reference to the number of nodes in a component (under a root).

- union(a, b): Merge the trees by making one node's root a parent of the other.
               Balanced: Merge the smaller tree into the larger tree by making
               the root of the larger tree the parent of the root of the
               smaller tree. This makes findRoot O(lg N).
- connected(a, b): Changes to utilize findRoot to compare the roots of a and b.

#### Balancing

Using trees works well, but still has O(N) worst case as the tree can
get N deep. If we keep the tree balanced while performing union/findRoot
operations, then we can make it so that the tree will not grow more than
O(lg N) deep. To do this, we make sure that the smaller component is
merged into the larger component. We have to keep track of and update
the size of each component.

### Optimization

When finding the root of a node, flatten the tree.

1. When finding the root of a node, keep track of the ancestors that are
traversed up the tree. Set their parent equal to the round root.

2. When traversing up the tree, set each node's ancestor to it's ancestor's
ancestor (move them all up by 1). This uses less memory and, in practice,
works just as well as #1.

## Proof notes

If you start at 1 and double lg N times, you get N.
Adding the smaller tree to the larger tree increased the depth of the
nodes on the smaller tree by one, but the size of the component increases
by at least half (from the perspective of the nodes in the smaller component).
Thus, the depth can only increase lg N times.

## Notes

lg\* n: Iterated log function. The number of times you take the log of a
number to get to 1. lg\* 2^65535 = 1 (near linear).
