from collections import defaultdict

def dist(s):
    d = defaultdict(int)
    for c in s:
        d[c] += 1
    return d

def remove(d, char):
    d[char] -= 1
    if d[char] == 0:
        del d[char]

def anagram_substr(W, S):
    sols = []
    for i in range(len(S)):
        coll = dist(W)
        if len(W) > len(S) - i:
            return sols
        for j in range(i, i+len(W)):
            char = S[j]
            if char not in coll:
                break
            remove(coll, char)
            if len(coll) == 0:
                sols.append(i)
    return sols


print(anagram_substr('ba', 'abxaba'))
