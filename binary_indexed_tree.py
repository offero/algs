"""
Implementation of a Binary Indexed Tree (Fenwick Tree).

This structure stores the running sum of an array.

Sum time: O(log(n))
Update time: O(log(n))
Extra space: O(n)
"""

def parentlt(idx):
    return idx - (idx & -idx)

def parentgt(idx):
    return idx + (idx & -idx)

class BIT(object):
    def __init__(self, arr):
        """arr: The list of numbers for which we create the BIT."""
        self._bit = [0] * (len(arr)+1)  # list of 0s
        for i in range(1, len(arr)+1):
            self.update_value(i, arr[i-1])

    def update_value(self, idx, val):
        """
        idx: BIT index (list index + 1)
        val: +/- amount (Amount of change of value at index i).
        """
        while idx < len(self._bit):
            self._bit[idx] += val
            idx = parentgt(idx)

    def get_sum(self, idx):
        """Return the sum up to BIT index idx (list index + 1)."""
        tot = 0
        while idx > 0:
            tot += self._bit[idx]
            idx = parentlt(idx)
        return tot
