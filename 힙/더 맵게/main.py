import heapq


def solution(scoville, K):
    pq = []
    for sv in scoville:
        heapq.heappush(pq, sv)

    cnt = 0
    size = len(scoville)
    while True:
        a = heapq.heappop(pq)
        if a >= K:
            return cnt

        if size < 2:
            return -1

        cnt += 1
        size -= 1
        b = heapq.heappop(pq)
        heapq.heappush(pq, a + b * 2)
