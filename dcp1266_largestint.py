'''
Given a list of numbers, create an algorithm that arranges them in order to form the largest
possible integer. For example, given [10, 7, 76, 415], you should return 77641510
'''

'''
all numbers with the largest left leading number
from that list, sort by the 2nd value from left
  if value > value to the left, then larger
  if value = value to the left, then equal
  else smaller

  7 > 76
  78 > 7

  456 456|4589

  456|4589 456

  456 458|9

'''
####################
# solution 2 - sort with comparator
# O(n*log(n))

from functools import cmp_to_key

def cmp(a, b):
    """returns -1 or 1 indicating the larger input value"""
    if len(a) == len(b):
        return 1 if a > b else -1

    i = min(len(a), len(b))
    if a[:i] > b[:i]:
        return 1

    if a[:i] == b[:i]:
        if len(a) < len(b):
            return cmp(a, b[i:])
        else:
            return cmp(a[i:], b)

    return -1

def largest_int_2(arr):
    svalues = list(map(str, arr))
    return int(''.join(list(sorted(svalues, key=cmp_to_key(cmp), reverse=True))))

#############################
# solution 1 - comparing every value
# O(N^2)

def compare(a, b):
    """returns the greater value"""
    if len(b) < len(a):
        a, b = b, a
    i = len(a)
    if a > b[:i]:
        return a
    if a == b[:i]:
        return compare(a, b[i:])
    return b


def largest_int(arr):
    svalues = list(map(str, arr))
    sol = []
    while svalues:
        m = svalues[0]
        for i in range(1, len(svalues)):
            m = compare(m, svalues[i])
        sol.append(m)
        svalues.remove(m)
    return int(''.join(sol))


sol1 = largest_int([10, 7, 76, 415])
print(sol1, sol1 == 77641510)

sol1 = largest_int_2([10, 7, 76, 415])
print(sol1, sol1 == 77641510)
