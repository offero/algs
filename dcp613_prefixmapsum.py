'''
Implement a PrefixMapSum class with the following methods:

insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:

mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5
'''

'''
Solution

Idea 1: For each key, check prefix, add
insert is O(1)
sum is O(n) (n: the number of words inserted)

Idea 2:
Use a prefix tree
Insert is O(w) (w: number of characters in a word)
Sum is O(w)
'''

#################### Sol 1

class PrefixMapSum1:
    def __init__(self):
        self.data = {}

    def insert(key, value):
        self.data[key] = value

    def sum(prefix):
        total = 0
        for (key, value) in self.data.items():
            if key.startswith(prefix):
                total += value
        return total

##################### Sol 2

class Node:
    def __init__(self, value=0):
        self.value = value
        self.children = {}

class PrefixMapSum2:
    def __init__(self):
        self.root = Node()

    def insert(self, word, value):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node(value)
            else:
                node.children[c].value += value
            node = node.children[c]

    def sum(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        return node.value

def test():
    tree = CountedPrefixTree()
    tree.insert('abcde', 4)
    tree.insert('abcfg', 3)
    print(tree.sum('a'))
    print(tree.sum('ab'))
    print(tree.sum('abc'))
    print(tree.sum('abcd'))
    print(tree.sum('abcf'))
    print(tree.sum('abcz'))


if __name__ == "__main__":
    test()
