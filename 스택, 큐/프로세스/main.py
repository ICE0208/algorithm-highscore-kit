from collections import deque


def solution(priorities, location):
    deq = deque()
    for i, pri in enumerate(priorities):
        deq.append((i, pri))

    cnt = 0
    while deq:
        cur_max = max([pri for i, pri in deq])
        cur = deq.popleft()
        if cur[1] == cur_max:
            cnt += 1
            if cur[0] == location:
                return cnt

        else:
            deq.append(cur)
