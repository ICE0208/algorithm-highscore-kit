def solution(sizes):
    a_max = 0
    b_max = 0
    for size_1, size_2 in sizes:
        a_max = max(a_max, max(size_1, size_2))
        b_max = max(b_max, min(size_1, size_2))
        
    return a_max * b_max