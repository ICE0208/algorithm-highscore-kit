from collections import deque


def solution(maps):
    answer = 10000
    moves = ((0, -1), (0, 1), (-1, 0), (1, 0))

    x_len = len(maps)
    y_len = len(maps[0])

    q = deque()
    maps[0][0] = 0
    q.append((0, 0, 1))

    while q:
        cur_x, cur_y, cost = q.popleft()
        if cur_x == x_len - 1 and cur_y == y_len - 1:
            answer = min(answer, cost)

        for move in moves:
            next_x, next_y = cur_x + move[0], cur_y + move[1]

            if not (0 <= next_x < x_len and 0 <= next_y < y_len):
                continue
            if maps[next_x][next_y] == 0:
                continue

            maps[next_x][next_y] = 0
            q.append((next_x, next_y, cost + 1))

    return -1 if answer == 10000 else answer
