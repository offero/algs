facts = {0: 1, 1: 1}

mod = 1000000007

def fact(n):
    if n not in facts:
        facts[n] = int((fact(n-1) * n) % mod)
    return facts[n]

if __name__ == "__main__":
    trials = int(input())
    for _ in range(trials):
        print(fact(int(input())))
