# 3번 문제
def get_primes(n):
    for i in range(n + 1):
        result = True
        if i < 2:
            result = False
        for j in range(2, i):
            if (i % j) == 0:
                result = False
        if result:
            print(i, end=' ')


get_primes(20)
