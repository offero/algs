# coding: utf-8

'''
Given Nodes such as


M->       N->       T->       D->       E
|          |         |        |	
C         X         Y          L
|         |
A         Z

-> right pointer 
| down pointer 

Output should be 
M->C->A->N->X->Z->T->Y->D-L>E 
'''

from __future__ import (absolute_import, division, print_function, unicode_literals)

def traverseInOrderR(node, order):
    order.append(node['name'])
    if 'left' in node:
        traverseInOrderR(node['left'], order)
    if 'right' in node:
        traverseInOrderR(node['right'], order)
    return order

def traverseInOrder(node):
    order = []
    stack = [node]
    while stack:
        node = stack.pop()
        order.append(node['name'])

        if 'right' in node:
            stack.append(node['right'])

        if 'left' in node:
            stack.append(node['left'])

    return order

nodes = {
    'name': 'M',
    'left': {
        'name': 'C',
        'left': {
            'name': 'A'
        }
    },
    'right': {
        'name': 'N',
        'left': {
            'name': 'X',
            'left': {
                'name': 'Z'
            }
        },
        'right': {
            'name': 'T',
            'left': {
                'name': 'Y'
            },
            'right': {
                'name': 'D',
                'left': {
                    'name': 'L'
                },
                'right': {
                    'name': 'E'
                }
            }
        }
    }
}

def main():
    print('->'.join(traverseInOrderR(nodes, [])))
    print('->'.join(traverseInOrder(nodes)))

if __name__ == '__main__':
    main()
