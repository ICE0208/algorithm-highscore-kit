def solution(participant, completion):
    hashmap = dict()
    for c in completion:
        hashmap[c] = 1 + hashmap.get(c, 0)
    for p in participant:
        if p not in hashmap:
            return p
        else:
            if hashmap[p] == 0:
                return p
            hashmap[p] -= 1
