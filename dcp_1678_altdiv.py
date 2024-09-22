def div(a, b):
    ct = 0
    while a >= b:
        a -= b
        ct += 1
    return ct

def bindiv(a, b):
    ct = 0
    shifts = 4
    while shifts:
        a = a - (b << shifts)
        shifts -= 1
        ct += 1
    return 2 ** ct


print(div(30,10))
print(div(30,5))
print(div(30,4))
print(div(30,2))
print(div(30,1))
