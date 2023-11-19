def solution(n, wires):
    g = [[] for _ in range(n + 1)]
    for wire in wires:
        g[wire[0]].append(wire[1])
        g[wire[1]].append(wire[0])

    result = n
    for i in range(0, len(wires)):
        v = []
        stack = []
        visited = set()
        for a in range(1, n + 1):
            if a in visited:
                continue
            visited.add(a)
            stack.append(a)
            cur_v = 1

            while stack:
                cur = stack.pop()
                for b in g[cur]:
                    if [cur, b] == wires[i] or [b, cur] == wires[i]:
                        continue
                    if b in visited:
                        continue
                    visited.add(b)
                    stack.append(b)
                    cur_v += 1
            v.append(cur_v)

        result = min(result, abs(v[0] - v[1]))
    return result
