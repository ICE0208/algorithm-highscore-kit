def solution(answers):
    p = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    scores = [0, 0, 0]

    for i, answer in enumerate(answers):
        for j in range(0, 3):
            if answer == p[j][i % len(p[j])]:
                scores[j] += 1

    result = []
    for i, score in enumerate(scores):
        if score == max(scores):
            result.append(i + 1)
    return result
