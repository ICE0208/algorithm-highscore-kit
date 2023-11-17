def solution(array, commands):
    result = []
    for command in commands:
        sub_array = array[command[0] - 1 : command[1]]
        sub_array.sort()
        result.append(sub_array[command[2] - 1])
    return result
