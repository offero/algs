'''
A network consists of nodes labeled 0 to N. You are given a list of edges (a, b,
t), describing the time t it takes for a message to be sent from node a to node
b. Whenever a node receives a message, it immediately passes the message on to a
neighboring node, if possible.

Assuming all nodes are connected, determine how long it will take for every node
to receive a message that begins at node 0.

For example, given N = 5, and the following edges:

edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5)
]

You should return 9, because propagating the message from 0 -> 2 -> 3 -> 4 will
take that much time.
'''
from typing import Set, Dict, List, Tuple

# TODO: Make an edge map instead for faster lookup
def neighbors(x, edges):
    return [(a,b,d) for (a,b,d) in edges if a==x]

def max_sp(edges):
    visited: Set[int] = set()
    sp_map: Dict[int, int] = dict()
    from_map: Dict[int, int] = dict()
    #            [distance from 0, to, from]
    to_visit: List[Tuple[int, int, int]] = [(0, 0, 0)]

    # run dfs on graph
    while to_visit:
        dist, t, f = to_visit.pop(0)
        if t not in sp_map or dist < sp_map[t]:
            # new shortest path to t
            sp_map[t] = dist
            from_map[t] = f

        for (a, b, d) in neighbors(t, edges):
            # cycle detection
            # don't add to list if longer than current solution
            if b in sp_map and dist+d > sp_map[b]:
                continue
            to_visit.append((dist+d, b, a))

        visited.add(t)

    print(sp_map)
    return max(sp_map.values())


edges = [
    (0, 1, 5),
    (0, 2, 3),
    (0, 5, 4),
    (1, 3, 8),
    (2, 3, 1),
    (3, 5, 10),
    (3, 4, 5),
    (5, 0, 1), # introduce cycle
]

ans = max_sp(edges)
print(ans)