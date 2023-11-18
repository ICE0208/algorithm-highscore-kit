def solution(prices):
    stack = []
    result = [0 for _ in range(len(prices))]
    for i, price in enumerate(prices):
        while stack and price < stack[-1][1]:
            poped = stack.pop()
            result[poped[0]] = i - poped[0]
        stack.append((i, price))

    while stack:
        poped = stack.pop()
        result[poped[0]] = len(prices) - 1 - poped[0]
    return result
