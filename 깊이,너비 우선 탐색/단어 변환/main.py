from collections import deque


def solution(begin, target, words):
    answer = 0
    words = set(words)
    q = deque()
    q.append((begin, 0))

    while q or words:
        cur_word, cost = q.pop()
        if cur_word == target:
            if answer == 0:
                answer = cost
            else:
                answer = min(answer, cost)
            break

        for idx in range(len(cur_word)):
            for c_n in range(ord("a"), ord("z") + 1):
                c = chr(c_n)
                next_word = cur_word[:idx] + c + cur_word[idx + 1 :]
                if next_word in words:
                    words.remove(next_word)
                    q.append((next_word, cost + 1))

    return answer
