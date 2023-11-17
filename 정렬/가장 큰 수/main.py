def solution(numbers):
    lst = []
    for i, number in enumerate(numbers):
        temp_list = str(number)
        length = len(temp_list)
        if length == 1:
            temp_list += "".join([temp_list[-1] for _ in range(3)])
        elif length == 2:
            temp_list += temp_list
        elif length == 3:
            temp_list += temp_list[0]
        lst.append((i, temp_list, length))

    # print(lst)
    lst.sort(key=lambda a: (a[1]), reverse=True)
    result = ""
    for l in lst:
        result += str(numbers[l[0]])
    for r in result:
        if r != "0":
            return result
    return "0"
