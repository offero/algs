fset = frozenset

def powerset(A):
    ps = set((fset(),))
    i = 0
    while i < len(A):
        i+=1
        new = set()
        for s in ps:
            for x in A:
                new.add(s.union(fset((x,))))
        ps.update(new)
    return ps

if __name__ == '__main__':
    A = [1,2,3]
    print(powerset(A))
