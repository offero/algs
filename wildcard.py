'''
Implement wildcard searching with ? and *
'''
tests = [
    ['aaxbb', 'aa*', True],
    ['aaxbb', '*bb', True],
    ['aaxbb', '???bb', True],
    ['aaxbb', '?*?bb', True],
    ['aaxbb', 'aax??', True],
    ['aaxb', 'aax??', False],
    ['aaxbb', 'aax?*', True],
    ['aaxbb', 'aa?bb', True],
    ['aaxxxbb', 'aa*bb', True],
    ['aaxxxbbxxxbb', 'aa*bb', True],
    ['aaxxxbbxxx', 'aa*bb', False],
    ['axbaxb', 'axb*axb', True],
    ['axbaxbaxb', 'axb*axb', True],
    ['axbaaaxbaxb', 'axb*axbaxb', True],
    ['aaxbb', 'aa?', False],
]

def matches(string, pattern, i=0, j=0):
    # if we are at the end of the pattern,
    # 1. if we are at the end of the string, True
    # 2. else, False
    if j >= len(pattern):
        if i >= len(string):
            # print('True 1')
            return True
        return False

    # if we are at the end of the string
    # 1. if we are at the end of the pattern (covered above)
    # 2. if the pattern character is a star, True
    if i >= len(string):
        if pattern[j] == '*' and j >= len(pattern):
            # print('True 2', i, j)
            return True
        return False

    if pattern[j] == '?':
        return matches(string, pattern, i+1, j+1)
    if pattern[j] == '*':
        # look ahead conditions
        # 1. end of the pattern
        # 2. next character is a ?
        # 3. next character is a *
        # 4. next character is a char
        if j+1 >= len(pattern):
            # print('True 3')
            return True #matches(string, pattern, i+1, j)

        if pattern[j+1] == '?':
            return matches(string, pattern, i+1, j) \
                or matches(string, pattern, i+1, j+1)

        if pattern[j+1] == '*':
            return matches(string, pattern, i+1, j+1)

        # next char is a char
        # find all occurrances in the string of that char and match from there
        for i2 in range(i, len(string)):
            # import ipdb; ipdb.set_trace()
            if string[i2] == pattern[j+1]:
                # print('matching', i2, j+1)
                if matches(string, pattern, i2, j+1):
                    # print('True 4')
                    return True

        return matches(string, pattern, i+1, j)

    if string[i] != pattern[j]:
        return False

    return matches(string, pattern, i+1, j+1)

for (string, pattern, expected_value) in tests:
    print(matches(string, pattern), expected_value)

