import heapq
from collections import deque


def solution(jobs):
    sec = 0
    jobs.sort()
    pq = []
    deq = deque(jobs)

    time = 0
    while deq or pq:
        while deq and (deq[0][0] <= sec):
            job = deq.popleft()
            heapq.heappush(pq, (job[1], job))
        if pq:
            poped = heapq.heappop(pq)
            time += sec - poped[1][0] + poped[1][1]
            sec += poped[1][1]
        else:
            sec += 1

    return time // len(jobs)
