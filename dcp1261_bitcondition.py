'''
DCP #1261
32 bit ints x, y, b
return x if b == 1
return y if b == 0
Use only math and bit operations
'''
def bitcond(x, y, b):
    # i could just spell this out on 32 lines so the loop is okay
    # convert b into all 1s or all 0s
    for i in range(32):
        b = b | b<<i
    # first part is either x+y or just y
    t1 = (x & b) + y
    # second part is either y or 0
    t2 = (b | y) - (b ^ y)
    return t1 - t2


print('received expected')
print(bitcond(4, 5, 1), 4)
print(bitcond(4, 5, 0), 5)

print(bitcond(123, 456, 1), 123)
print(bitcond(123, 456, 0), 456)
