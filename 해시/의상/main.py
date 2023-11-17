def solution(clothes):
    hashmap = dict()

    for name, type in clothes:
        hashmap[type] = hashmap.get(type, 0) + 1

    result = 1
    for v in hashmap.values():
        result *= v + 1

    return result - 1
