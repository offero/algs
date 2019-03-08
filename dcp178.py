from __future__ import division, print_function
'''
Question
########

This problem was asked by Two Sigma.

Alice wants to join her school's Probability Student Club. Membership dues are computed via one of
two simple probabilistic games.

The first game: roll a die repeatedly. Stop rolling once you get a five followed by a six. Your
number of rolls is the amount you pay, in dollars.

The second game: same, except that the stopping condition is a five followed by a five.

Which of the two games should Alice elect to play? Does it even matter? Write a program to simulate
the two games and calculate their expected value.

Answer
######

Assumption: The die is a *fair* die and there is a uniform probability of 1/6 that each number [1, 6]
will show up on any given roll.

1st scenario: P(5) = 1/6 & P(6) = 1/6. P(5) and P(6) = 1/6 * 1/6
2nd scenario: P(6) = 1/6 & P(6) = 1/6. P(6) and P(6) = 1/6 * 1/6

The two games are the same because every roll is its own independent event.
'''

import random

def sim(a=5, b=6):
    ct = 0
    while True:
        ct += 1
        exa = random.randint(1, 6)
        exb = random.randint(1, 6)
        if exa == a and exb == b:
            return ct

if __name__ == '__main__':
    print(1./(1./6 * 1./6))
    n = 6000
    print(sum((sim(5, 5) for _ in range(n)))/n)
    print(sum((sim(6, 6) for _ in range(n)))/n)
