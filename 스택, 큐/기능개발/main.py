import math


def solution(progresses, speeds):
    lst = []
    result = []
    for pro, spe in zip(progresses, speeds):
        remain = math.ceil((100 - pro) / spe)
        if len(lst) == 0:
            lst.append(remain)
        else:
            if remain <= lst[0]:
                lst.append(remain)
            else:
                result.append(len(lst))
                lst.clear()
                lst.append(remain)

    if lst:
        result.append(len(lst))

    return result
