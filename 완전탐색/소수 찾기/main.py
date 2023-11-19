from itertools import permutations


def solution(numbers):
    result = set()

    isPrime = [True for _ in range(10000000)]
    for i in range(0, 2):
        isPrime[i] = False

    for i in range(2, len(isPrime)):
        if isPrime[i] == False:
            continue
        for j in range(i + i, len(isPrime), i):
            isPrime[j] = False

    for i in range(1, len(numbers) + 1):
        for s in permutations(numbers, i):
            if isPrime[int("".join(s))]:
                result.add(int("".join(s)))
    return len(result)
