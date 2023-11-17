def solution(genres, plays):
    # dict -> 나중에 전체 재생수 기준으로 sort
    # key: genres
    # value : (전체 재생수, [(재생수, 고유 번호)]) -> 나중에 (-재생수, 고유 번호) 기준으로 sort
    hashmap = dict()
    for genre, play, i in zip(genres, plays, range(0, len(plays))):
        if genre not in hashmap:
            hashmap[genre] = (0, [])

        hashmap[genre] = (hashmap[genre][0] + play, hashmap[genre][1] + [(play, i)])

    result = []
    genre_list = list(sorted(list(hashmap.values()), key=lambda a: -a[0]))
    for i in range(0, len(genre_list)):
        play_list = list(sorted(genre_list[i][1], key=lambda a: (-a[0], a[1])))
        for j in range(0, len(play_list)):
            if j == 2:
                break
            result.append(play_list[j][1])
    return result
