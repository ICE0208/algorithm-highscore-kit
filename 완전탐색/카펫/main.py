def solution(brown, yellow):
    for y in range(1, yellow + 1):
        if yellow % y != 0:
            continue
        x = yellow // y
        if x + y + 2 == brown // 2:
            return [x + 2, y + 2]


# x+2, y+2
# x * y = yellow
# 2x+2y+4 = brown
# x+y+2 = brown/2
