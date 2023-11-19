def bt(remain_k, n, visited):
    if len(visited) >= len(dungeons):
        global result
        result = max(result, n)
        return

    for next in range(0, len(dungeons)):
        if next in visited:
            continue

        visited.add(next)
        if dungeons[next][0] <= remain_k:
            bt(remain_k - dungeons[next][1], n + 1, visited)
        bt(remain_k, n, visited)
        visited.remove(next)


def solution(k, d):
    global dungeons
    global result
    dungeons = d
    result = 0

    bt(k, 0, set())
    return result
