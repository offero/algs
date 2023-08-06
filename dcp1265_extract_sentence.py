def extract_words(sentence, dictionary, words=None):
    if words is None:
        words = []
    if not sentence:
        return True, words
    if not dictionary:
        return False, words
    for i in range(1, len(sentence)+1):
        prefix = sentence[:i]
        if prefix not in dictionary:
            continue
        words.append(prefix)
        dictionary.remove(prefix)
        sol, _ = extract_words(sentence[i:], dictionary, words)
        if sol:
            return True, words
        words.pop()
        dictionary.append(prefix)
    return False, words


ex1 = {
    "sentence": "thequickfoxesrun",
    "dictionary": ["quick", "fox", "foxes", "run", "the"]
}

ex2 = {
    "sentence": "bedbathandbeyond",
    "dictionary": ["bed", "bedbath", "and", "bath", "beyond"]
}

for ex in [ex1, ex2]:
    sol, words = extract_words(ex['sentence'], ex['dictionary'])
    print(sol, words)
