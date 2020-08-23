'''
Given a string of parentheses, write a function to compute the minimum number of parentheses to be removed to make the string valid (i.e. each open parenthesis is eventually closed).

For example, given the string "()())()", you should return 1. Given the string ")(", you should return 2, since we must remove all of them.
'''

def minparen(s):
    invalid = 0
    count = 0
    for char in s:
        if char == ')':
            if count == 0:
                invalid += 1
            else:
                count -= 1
        else: # '('
            count += 1
    return invalid + count

if __name__ == "__main__":
    print(minparen('()())()') == 1)
    print(minparen(')(') == 2)
    print(minparen('))(()(()') == 4)
