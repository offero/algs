'''
You are given an array of nonnegative integers. Let's say you start at the beginning of the array
and are trying to advance to the end. You can advance at most, the number of steps that you're
currently on. Determine whether you can get to the end of the array.

For example, given the array [1, 3, 1, 2, 0, 1], we can go from indices 0 -> 1 -> 3 -> 5, so return
true.

Given the array [1, 2, 1, 0, 0], we can't reach the end, so return false.


Constraints/Assumptions:

Array of positive ints.
Fits in memory.

Examples:

[1, 3, 1, 2, 0, 1]
 X  X  -  -  -

Ideas:

Stack with position indices (BFS/DFS).

Dynamic programming.

Recursion.
  reachable([1, 3, 1, 2, 0, 1])
  = reachable([3, 1, 2, 0, 1])

  reachable([3, 1, 2, 0, 1])
  = reachable([1, 2, 0, 1]) || reachable([2, 0, 1]) || reachable([0, 1])

  reachable([1, 2, 0, 1])
  = reachable([2, 0, 1])

  +++++++++++++++++++

  reachableFromIndex(0, array)
  = reachableFromIndex(1, array)

  reachableFromIndex(1, array)
  = reachableFromIndex(2, array)
    || reachableFromIndex(3, array)
    || reachableFromIndex(4, array)

  reachableFromIndex(2, array)
  = reachableFromIndex(3, array)
'''

def reachableBFS(arr):
    stack = [0]  # indices
    visited = set([0])  # non-exponential

    while stack:
        thisidx = stack.pop()
        visited.add(thisidx)

        if thisidx == len(arr)-1:
            return True

        steps_to_take_from_here = arr[thisidx]
        for step in range(1, steps_to_take_from_here+1):
            nextidx = step + thisidx
            if nextidx not in visited:
                stack.append(nextidx)  # append = BFS

    return False

def test():
    ex1 = [1, 3, 1, 2, 0, 1]
    print(reachableBFS(ex1))

    ex2 = [1, 2, 1, 0, 0]
    print(reachableBFS(ex2))

if __name__ == '__main__':
    test()
