"""
Introduction to Algorithms A Creative Approach by Udi Manber

Exercise 4.27

Let A [1..n] be an array of real numbers. Design algorithms to perform
any sequence of the following two operations:

    Add(i, y): add the value y to the i'th number.
    Partial_sum(i): return the sum of the first i numbers

The number of elements is fixed.
Each operation should take O(log n) steps.
You can use one more array of size n as work space.
"""

from math import pow, ceil, log

def parent(i):
    return i//2

def rchild(i):
    return 2*i + 1

def lchild(i):
    return 2*i

def construct_tree(arr):
    exp = ceil(log(len(arr), 2))
    closest_power_of_2 = 2**exp
    extra =  closest_power_of_2 - len(arr)
    tree = ([0] * closest_power_of_2) + arr + ([0] * extra)
    for i in range(len(tree)-1, 1, -1):
        j = parent(i)
        tree[j] += tree[i]
    return tree

def is_right_child(tree, i):
    return rchild(parent(i)) == i

def is_left_child(tree, i):
    return lchild(parent(i)) == i

def is_root(tree, i):
    return i == 1

def partial_sum(tree, i):
    start = len(tree)//2
    i = start + i
    agg = 0

    while not is_root(tree, i):
        if is_right_child(tree, i):
            i = parent(i)
        if is_left_child(tree, i):
            agg -= tree[rchild(parent(i))]
            i = parent(i)

    return tree[1] + agg

def add(tree, i, value):
    start = len(tree)//2
    i = start + i
    while not is_root(tree, i):
        tree[i] += value
        i = parent(i)
    tree[i] += value


if __name__ == "__main__":
    tree = construct_tree([3,9,4,2,1,6,7])
    print(tree)
    # print(partial_sum(tree, 0))
    # print(partial_sum(tree, 1))
    # print(partial_sum(tree, 2))
    # print(partial_sum(tree, 3))
    # print(partial_sum(tree, 4))
    # print(partial_sum(tree, 5))
    # print(partial_sum(tree, 6))
    add(tree, 3, 10)
    print(tree)

