"""
Testing binary algorithms in Python (because the repl an ipython rocks).
"""

def clear_last_bit(x):
    """Zeros the least significant bit.

    >>> clear_last_bit(0b10100000) == 0b10000000
    True
    >>> clear_last_bit(0b10110000) == 0b10100000
    True
    """
    return x & (x-1)

def lowest_set_bit(x):
    """
    >>> lowest_set_bit(0b0111) == 0b0001
    True
    >>> lowest_set_bit(0b0110) == 0b0010
    True
    """
    return x & ~(x-1)

def fold_over(x):
    """Sets all bits after the most significant.

    >>> fold_over(0b001001010) == 0b001111111
    True
    """
    for i in range(0, 6):
        x |= (x >> 2**i)
    return x

def next_power_of_2(x):
    """
    >>> next_power_of_2(0)
    1
    >>> next_power_of_2(1)
    2
    >>> next_power_of_2(2)
    4
    >>> next_power_of_2(3)
    4
    >>> next_power_of_2(10)
    16
    """
    return fold_over(x)+1

def highest_set_bit(x):
    """
    >>> highest_set_bit(0b00110011) == 0b00100000
    True
    >>> highest_set_bit(0b01010000) == 0b01000000
    True
    >>> highest_set_bit(0b00000001) == 0b00000001
    True
    """
    return (fold_over(x)+1) >> 1

def log_2(x):
    """Integer log base 2 (positive only).
    >>> all((log_2(0)==0, log_2(1)==0, log_2(2)==1, log_2(15)==3, log_2(16)==4))
    True
    """
    ct = 0
    if x <= 0:
        return 0

    while x:
        ct, x = ct+1, x >> 1
    return ct-1


def mult1(x, y):
    """Multiplication without * (positive only)

    >>> [mult1(0, i) for i in range(10)] == [0] * 10
    True
    >>> [mult1(1, i) for i in range(10)] == list(range(10))
    True
    >>> [mult1(2,i) for i in range(10)] == [2*i for i in range(10)]
    True
    >>> [mult1(3,i) for i in range(10)] == [3*i for i in range(10)]
    True
    """
    if x < 0 or y < 0:
        raise Exception("Positive only")

    total = 0
    shift = 0
    while y:
        if y & 1:
            total += (x << shift)
        y = (y >> 1)
        shift += 1

    return total

def mult2(x, y):
    """
    >>> [mult2(0, i) for i in range(10)] == [0] * 10
    True
    >>> [mult2(1, i) for i in range(10)] == list(range(10))
    True
    >>> [mult2(2,i) for i in range(10)] == [2*i for i in range(10)]
    True
    >>> [mult2(3,i) for i in range(10)] == [3*i for i in range(10)]
    True
    """
    total = 0
    while y:
        total += (x << log_2(lowest_set_bit(y)))
        y = clear_last_bit(y)
    return total
