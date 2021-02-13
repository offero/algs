#!/usr/bin/env python3
"""
This problem was asked by Google.

You are given a set of synonyms, such as (big, large) and (eat, consume). Using this set, determine if two sentences with the same number of words are equivalent.

For example, the following two sentences are equivalent:

    "He wants to eat food."
    "He wants to consume food."

Note that the synonyms (a, b) and (a, c) do not necessarily imply (b, c): consider the case of (coach, bus) and (coach, teacher).

Follow-up: what if we can assume that (a, b) and (a, c) do in fact imply (b, c)?
"""

"""
Observations
- Same sentence length (check this first)

Clarifications
- What is the synonym input exactly?
    "A set of synonyms"
    {(big, large), (eat, consume)}
    [(big, large, huge), (eat, consume), (food, dinner, breakfast, lunch)]
    [(big, large), (big, huge)] ...

Examples

    Synonyms:
        (big, large), (eat, consume)

    "He wants to eat food."
    "He wants to consume food."
    > True

    "He wants to prepare dinner."
    "He wants to consume food."
    > False

    "He wants to eat food!"
    "He wants to consume food."
    > False

Approaches
- pass through the sentences once
- check boundary conditions
    - sentence length
- tokenize the sentence
- create a way to look up synonyms fast

synonyms = {
    big: 1,
    large: 1,
    eat: 2,
    consume: 2,
}

"""

import string

EXAMPLES = [
    ( # True with synonym match
        "He wants to eat food.",
        "He wants to consume food.",
        [("big", "large"), ("eat", "consume")],
        True,
    ),
    ( # False with synonym match but word mismatch
        "He wants to eat dinner.",
        "He wants to consume food.",
        [("big", "large"), ("eat", "consume")],
        False,
    ),
    ( # False due to punctuation mismatch
        "He wants to eat food!",
        "He wants to consume food.",
        [("big", "large"), ("eat", "consume")],
        False,
    ),
]

def tokenize(sent):
    # split on space
    # remove extra space
    # handle punctuation, multiple spaces
    tokens = []
    token = []
    for char in sent:
        if char in string.punctuation: # handle puntuation
            tokens.append(''.join(token))
            token.clear()
            tokens.append(char)
        elif char == ' ': # handle spaces
            if tokens and tokens[-1] == ' ':
                continue
            tokens.append(''.join(token))
            token.clear()
        else: # assume valid word characters
            token.append(char)

    # end of sentence
    if token:
        tokens.append(''.join(token))
        token.clear()
    return tokens

def create_syn_map(syns):
    syn_map = {}
    for i, synset in enumerate(syns):
        for word in synset:
            syn_map[word] = i
    return syn_map

def equivalent_sentences(sent1, sent2, syns):
    # tokenize sentences
    sent1_tok = tokenize(sent1)
    sent2_tok = tokenize(sent2)

    # check length and maybe bail
    if len(sent1_tok) != len(sent2_tok):
        return False

    # create synonym quick lookup structure
    syn_map = create_syn_map(syns)

    # scan through sentences
    for word1, word2 in zip(sent1_tok, sent2_tok):
        # if word match, continue
        if word1 == word2:
            continue
        # if not, check syn
        if word1 in syn_map and \
            word2 in syn_map and \
            syn_map[word1] == syn_map[word2]:
                continue
        return False

    return True

def main():
    for i, (sent1, sent2, syns, expected_value) in enumerate(EXAMPLES):
        result = equivalent_sentences(sent1, sent2, syns)
        if result != expected_value:
            print(f"Example {i} fail")
        else:
            print(f"Example {i} success")

if __name__ == "__main__":
    main()