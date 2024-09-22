'''

Implement a data structure which carries out the following operations without resizing the
underlying array:

add(value): Add a value to the set of values.
check(value): Check whether a value is in the set.

The check method may return occasional false positives (in other words, incorrectly identifying an
element as part of the set), but should always correctly identify a true element.
'''
from hashlib import md5, sha256

M = 256

def h1(value, fn=md5):
    if isinstance(value, str):
        value = value.encode('utf-8')
    return hash(fn(value))

def h2(value):
    return h1(value, fn=sha256)

class Bloom:
    def __init__(self):
        self.data = [0] * M

    def add(self, value):
        a = h1(value) % M
        b = h2(value) % M
        self.data[a] = 1
        self.data[b] = 1

    def check(self, value):
        a = h1(value) % M
        b = h2(value) % M
        return self.data[a] == 1 and self.data[b] == 1


b = Bloom()
b.add('hello')
b.add('world')

print(b.check('hello'))
print(b.check('worl'))
