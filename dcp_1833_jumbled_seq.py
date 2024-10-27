'''
DCP #1833
The sequence [0, 1, ..., N] has been jumbled, and the only clue you have for its
order is an array representing whether each number is larger or smaller than the
last. Given this information, reconstruct an array that is consistent with it.
For example, given [None, +, +, -, +], you could return [1, 2, 3, 0, 4]

Approaches
* Heuristic with look back O(n^2)
  * Requires some less memory, more runtime
* Heuristic with swapping and shifting 2n = O(n)
  * Requires some more memory, less runtime
'''

examples = [
    ['N', '+', '+', '-', '+'],
    ['N', '-', '-', '+', '-'],
    ['N', '-', '-', '-', '-'],
    ['N', '+', '+', '+', '+'],
    ['N', '-', '+', '-', '+'],
    ['N', '+', '-', '+', '-'],
]

'''

[0]
[0, 1] -> [1, 0]
[1, 0, 2] -> [X, 1, 0] -> [2, 1, 0]  shift right from previous plus, insert max at previous plus position

[0, 1, 2, 3, 4]
[0]
[0, 1]
[0, 1, 2]
[1, 2, 3, 0]
[1, 2, 3, 0, 4]

[0]
[0, 1]
[0, 1, 2] -swap(2,1)-> [0, 2, 1]
[0, 2, 1, 3]
[0, 2, 1, 3, 4] -swap(4,3)-> [0, 2, 1, 4, 3] swap max with previous plus


minus -> Min of all previous numbers. Increment all previous numbers.
plus -> max of all previous numbers + 1
'''

def solution1(lsarr):
    ans = [0]
    # assume first element is always "N"
    for i, op in enumerate(lsarr[1:]):
        if op == '+':
            ans.append(i + 1)
        else:
            ans.append(0)
            for j in range(len(ans)-1):
                ans[j] += 1
    return ans

def solution2(lsarr):
    ans = [0]
    pos_last_plus = 0
    # assume first element is always "N"
    for i, op in enumerate(lsarr[1:]):
        if op == '+':
            ans.append(i + 1)
            pos_last_plus = i+1
        else:
            #ans = ans[:pos_last_plus] + [i+1] + ans[pos_last_plus:]
            ans.append(None)
            for j in range(len(ans)-1, pos_last_plus, -1):
                ans[j] = ans[j-1]
            ans[pos_last_plus] = i + 1
    return ans

if __name__ == "__main__":
    for lsarr in examples:
        print(lsarr)
        print(solution1(lsarr))
        print(solution2(lsarr))
        print()