def solution(s):
    open_cnt = 0
    for c in s:
        if c == "(":
            open_cnt += 1
        else:  # c==")"
            open_cnt -= 1
            if open_cnt < 0:
                return False

    if open_cnt > 0:
        return False
    else:
        return True
