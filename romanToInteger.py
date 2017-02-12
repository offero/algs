roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# rules
# I before V or X means 1 less
# X before L or C means 10 less
# C before D or M means 100 less

exceptions = {
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900
}

test_strings = {
    'III': 3,
    'IV': 4,
    'V': 5,
    'VI': 6,
    'IX': 9,
    'X': 10,
    'XX': 20,
    'XL': 40,
    'XC': 90,
    'XD': 510
}

def romanToInteger(romanStr):
    total = 0
    i = 0
    while(i < len(romanStr)):
        c = romanStr[i]
        isLastChar = i == (len(romanStr)-1)

        if not isLastChar:
            nextC = romanStr[i+1]
            combo = (c + nextC)
            if combo in exceptions:
                total += exceptions[combo]
                i += 2
                continue

        total += roman_values[c]
        i += 1

    return total

def runTestCases():
    with open('./romanTestCases.txt') as fp:
        for line in fp:
            r, v = line.split(',')
            v = int(v)
            v2 = romanToInteger(r)
            assert v == v2, '%s %s %s' % (r, v, v2)

if __name__ == "__main__":
    cases = int(raw_input())
    for _ in range(cases):
        print(romanToInteger(raw_input()))
