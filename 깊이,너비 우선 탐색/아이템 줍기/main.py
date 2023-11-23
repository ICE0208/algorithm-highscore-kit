from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    for i, rec in enumerate(rectangle):
        rectangle[i] = list(map(lambda x: x * 2, rectangle[i]))

    maps = [[0 for i in range(101)] for j in range(101)]
    for rec in rectangle:
        for x in range(rec[0], rec[2] + 1):
            for y in range(rec[1], rec[3] + 1):
                maps[x][y] = 1

    for rec in rectangle:
        for x in range(rec[0] + 1, rec[2]):
            for y in range(rec[1] + 1, rec[3]):
                maps[x][y] = 0

    q = deque()
    q.append((characterX, characterY, 0))
    maps[characterX][characterY] = 0

    moves = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while q:
        cur_x, cur_y, cost = q.popleft()

        if cur_x == itemX and cur_y == itemY:
            return cost // 2

        for move in moves:
            next_x, next_y = cur_x + move[0], cur_y + move[1]
            if not (0 <= next_x <= 100 and 0 <= next_y <= 100):
                continue
            if maps[next_x][next_y] == 0:
                continue
            maps[next_x][next_y] = 0
            q.append((next_x, next_y, cost + 1))

    return -1
