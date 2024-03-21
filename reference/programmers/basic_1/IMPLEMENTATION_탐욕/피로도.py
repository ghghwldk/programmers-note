from itertools import permutations

def solution(k, dungeons):
    answer = 0

    dun_len = len(dungeons)

    for dungeonsCase in permutations(dungeons, dun_len):
        hp = k
        count = 0

        for dungeon in dungeonsCase:
            # 현재 피로도가 최소 필요도 이상일 경우
            if hp >= dungeon[0]:
                # 소모 필요도 차감
                hp -= dungeon[1]
                count += 1
            # 최댓값 갱신
            if count > answer:
                answer = count

    return answer