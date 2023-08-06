'''
You are given an array of nonnegative integers. Let's say you start at the beginning of the array
and are trying to advance to the end. You can advance at most, the number of steps that you're
currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return
true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.
'''

def reachable(arr, pos=0):
    if pos == len(arr)-1:
        return True

    steps = arr[pos]
    for i in range(1, steps+1):
        if reachable(arr, pos+i):
            return True

    return False


print(reachable([1, 3, 1, 2, 0, 1]))
print(reachable([1, 2, 1, 0, 0]))


"""
A more time efficient version that iterates backwards.
"""
def reachable_b(arr):
    r = [False] * len(arr)
    r[-1] = True
    # loop through the array backwards to fill in reachability
    for i in range(len(arr)-2, -1, -1):
        # is there a point from this point that reaches the end?
        for add in range(1, arr[i]+1):
            j = i+add
            if r[j]:
                r[i] = True
                break

    return r[0]

print(reachable_b([1, 3, 1, 2, 0, 1]))
print(reachable_b([1, 2, 1, 0, 0]))
