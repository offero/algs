'''
Write a function, add_subtract, which alternately adds and subtracts curried arguments. Here are some sample operations:
add_subtract(7) -> 7
add_subtract(1)(2)(3) -> 1 + 2 - 3 -> 0
add_subtract(-5)(10)(3)(9) -> -5 + 10 - 3 + 9 -> 11
'''

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

class add_sub:

    def __init__(self, x):
        self.op = add
        self.i = 0
        self.acc = x

    def __call__(self, x=None):
        if x is None:
            return self.acc

        self.acc = self.op(self.acc, x)
        self.i += 1
        self.op = self.i % 2 == 0 and add or sub
        return self

    def __str__(self):
        return str(self.acc)

print(add_sub(7))

print(add_sub(1)(2)(3))

print(add_sub(-5)(10)(3)(9))


