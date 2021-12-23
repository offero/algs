'''
DCP 1043

Given an iterator with methods next() and hasNext(), create a wrapper iterator, PeekableInterface,
which also implements peek(). peek shows the next element that would be returned on next().
'''

class Placeholder:
    pass

EMPTY = Placeholder()

class PeekableInterface(object):
    def __init__(self, iterator):
        self.it = iterator
        self.buffer = EMPTY

    def peek(self):
        if self.buffer is not EMPTY:
            return self.buffer
        self.buffer = self.it.next()
        return self.buffer

    def next(self):
        if self.buffer is not EMPTY:
            value = self.buffer
            self.buffer = EMPTY
            return value
        return self.it.next()

    def hasNext(self):
        if self.buffer is not EMPTY:
            return True
        return self.it.hasNext()

class ThingIterator:
    def __init__(self):
        self.values = [1, 2, 3, 4]
    
    def next(self):
        return self.values.pop()

    def hasNext(self):
        return bool(self.values)


def main():
    ti = ThingIterator()
    pi = PeekableInterface(ti)
    print(pi.hasNext(), pi.peek(), pi.next())
    print(pi.hasNext(), pi.peek())
    print(pi.hasNext(), pi.next())
    print(pi.hasNext(), pi.peek(), pi.next())
    print(pi.hasNext(), pi.next())
    print(pi.hasNext())

if __name__ == "__main__":
    main()
