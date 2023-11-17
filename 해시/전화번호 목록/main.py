def solution(phone_book):
    hashset = set()
    for phone in phone_book:
        s = ""
        for c in phone:
            s += c
            if s == phone:
                continue
            hashset.add(s)

    for phone in phone_book:
        if phone in hashset:
            return False
    return True
