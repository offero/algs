'''
Find the minimum number of changes required to balance a string of braces
'{' and '}'.


Solved using Dynamic Programming

#####
}}}}} {{{{{
{}{}{ }{}{}
    3     6

######
}}{{{{
{}{}{}
1  2 3

######
}}}{
{}{} or {{}}
1 23    12 3

Keep track of right paren that don't have a corresponding left paren.
Each time a } is encountered such that the count for { is 0, then imbalance++.

bal(s) = {
    "{}": 0,
    "}}": 1,
    "{{": 1,
    "}{": 2
}

rbal(s) = # right balances

nbal(s) = min {
    nbal(s[:l-2]) + bal(s[l-2:]),
    "}}": nbal(s[:l-2]) - 1 if rbal(s[:l-2]) > 0
    "}{": nbal(s[:l-2]) - 1 + 1 if rbal(s[:l-2]) > 0  (Moot? Does this do anything?)
}

'''

def twos(s):
    it = iter(s)
    while True:
        yield (next(it), next(it))

bal = {
    "{}": 0,
    "}}": 1,
    "{{": 1,
    "}{": 2
}

# Number of left braces changed into right braces in order to balance a pair.
# We only need to keep track of the changes to right braces.
rbal = {
    "{}": 0,
    "}}": 0,
    "{{": 1,
    "}{": 1
}

def balance_dp(s):
    prev = cur = 0

    # rb: number of times we switched a '{' to a '}'
    rb = 0
    for i, (a,b) in enumerate(twos(s)):
        if i == 0:
            # balanced[i] = bal[a+b]
            cur = bal[a+b]

        if a+b == "}}" and rb > 0:
            # undo 1 previous right brace change
            # balanced[i] = balanced[i-1]-1
            cur = prev - 1
            rb -= 1
        elif a+b == "}{" and rb > 0:
            # undo 1 previous right brace change
            # but we still have to balance 1 paren
            # balanced[i] = balanced[i-1]
            cur = prev
            rb -= 1
        else:
            # balanced[i] = balanced[i-1] + bal[a+b]
            cur = prev + bal[a+b]
            rb += rbal[a+b]

        prev = cur

    # print(balanced)
    return cur


test_cases = {
    "": 0,
    "{}": 0,
    "{{": 1,
    "}}": 1,
    "}{": 2,

    "}}{}": 1,
    "}}}}": 2,
    "}}{{": 2,
    "}}}{": 3,

    "{{{}}}": 0,
    "{{{}{{": 2,
    "{{{}{}": 1,
    "{{{}}{": 1,
    "}}{}}}": 2,

    "}}}}}{{{{{": 6
}

def test_balance_dp():
    for s, v in test_cases.items():
        res = balance_dp(s)
        assert res == v, "Test Case fail %s. Expected %d Returned %d" % (s, v, res)
