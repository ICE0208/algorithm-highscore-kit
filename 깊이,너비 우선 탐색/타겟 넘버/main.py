def dfs(s, idx):
    if idx == len(numbers):
        if s == target:
            global answer
            answer += 1
        return

    dfs(s + numbers[idx], idx + 1)
    dfs(s - numbers[idx], idx + 1)


def solution(n, t):
    global target, numbers, answer
    numbers, target = n, t
    answer = 0

    dfs(0, 0)
    return answer
