## 더 맵게

[🔗 링크](https://school.programmers.co.kr/learn/courses/30/lessons/42626)

우선순위 큐를 사용해야할 것 같아서 파이썬 priorityqueue를 찾아서 구현했다.

```python
from queue import PriorityQueue
def solution(scoville, K):
    pq = PriorityQueue()
    for sv in scoville:
        pq.put(sv)

    cnt = 0
    size = len(scoville)
    while True:
        a = pq.get()
        if a >= K:
            return cnt

        if size < 2:
            return -1

        cnt += 1
        size -= 1
        b = pq.get()
        pq.put(a+b*2)
```

근데 시간초과가 났다! 인터넷에 찾아보니 heapq로 구현하면 좀 더 빠르다고 한다. 이유는 PriorityQueue는 Thread-Safe를 보장하기 때문에 시간이 좀 더 걸린다고 한다. 그래서 heapq를 사용하여 아래와 같이 구현하였다.

```python
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

```

사실 heapq도 사용법이 기억이 안나서 찾아보았다. 잘 알아둘 것.
