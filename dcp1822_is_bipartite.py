'''
Determine if an undirected graph G is bipartite.
'''

def neighbors_of_group(G, group):
    neighbors = set()
    for v in group:
        for u in G[v]:
            neighbors.add(u)
    return neighbors

def is_bipartite(G):
    U, V = set(), set()
    to_visit = set(G.keys()) # we should visit all nodes once
    visited = set() # we should not visit the same node twice
    # select a starting node
    group = {next((k for k in G.keys()))}
    while len(to_visit) > 0:
        U.update(group)
        visited.update(group)
        to_visit.difference_update(group)
        # add all neighbors from the previous group
        group = neighbors_of_group(G, group)
        # if there are no new neighbors to visit
        if len(group - visited) == 0:
            # if the graph is disconnected, pick another node
            if to_visit:
                group = {next((x for x in to_visit))}
            else:
                break
        U, V = V, U

    print(U)
    print(V)
    if len(U.intersection(V)) == 0:
        return True
    return False

bp1 = {
    'a': ['b'],
    'b': ['c'],
    'c': ['d', 'e'],
    'd': [],
    'e': []
}
# U: a, c
# V: b, d, e

a = is_bipartite(bp1)
print(a)