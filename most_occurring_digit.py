"""
Challenge: Find the most occuring digit in an integer without using an array,
hashmap, or string.

Strategy:
"""
places = 20  # Max number of decimal places in 64 bit int.

def most_occuring_digit(v):

    max_digit = None
    max_ct = 0

    for i in range(10): # 0 through 9
        ct = 0
        for j in range(1, places): # places
            f = v // ((10**j)//10)  # The part of v we care about
                                    # (Chop off the right side)
            if f == 0:
                break

            f = f - (f // 10) * 10  # The digit we care about
            if i == f:
                ct += 1

        if ct > max_ct:
            max_digit = i
            max_ct = ct

    return (max_digit, max_ct)
