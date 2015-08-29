#!/usr/bin/env python

import numpy as np
from functools import reduce
from operator import mul

def fib_mat(n):
    """Fibonacci; matrix style. O(n)"""
    a = np.matrix([[1, 1],  # the first elt + the second (cur fib no.)
                   [1, 0]]) # the first elt (prev fib no.)
    b = np.matrix([[1,1]])
    return reduce(mul, [b] + [a]*n)[0,0]
