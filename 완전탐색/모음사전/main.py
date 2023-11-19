def dfs(w, n):
    global cnt
    if target_word == w:
        global result
        result = cnt
    cnt += 1

    if n == 5:
        return
    for next in "AEIOU":
        dfs(w + next, n + 1)


def solution(word):
    global target_word
    target_word = word
    global cnt
    cnt = 0
    global result

    dfs("", 0)

    return result
