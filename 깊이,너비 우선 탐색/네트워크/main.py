from collections import deque


def solution(n, computers):
    answer = 0
    q = deque()

    visit = [False for _ in range(n)]
    for start in range(n):
        if visit[start] == True:
            continue
        visit[start] = True
        answer += 1
        q.append(start)
        while q:
            cur = q.popleft()

            for nxt in range(0, n):
                if visit[nxt] == True or computers[cur][nxt] == 0:
                    continue
                visit[nxt] = True
                q.append(nxt)

    return answer
