def solution(citations):
    citations.sort(reverse=True)
    index = 0
    cnt = 0  # h번 이상 인용된 논문의 수
    for i in range(10000, -1, -1):
        while citations[index] >= i:
            cnt += 1
            index += 1
            if index >= len(citations):
                return min(i, cnt)
        if cnt >= i:
            return i
