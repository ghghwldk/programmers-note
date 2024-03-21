def solution(picks, minerals):
    # 광물의 수가 (곡괭이의 수) x 5 보다 많다면,
    # 채굴 가능한 총 광물의 개수를 자원 (곡괭이의 수) x 5로 제한한다.
    if sum(picks) * 5 < len(minerals):
        minerals = minerals[:sum(picks) * 5]

    # 광물을 크기가 5인 청크로 분할하고 각 청크에 포함된 종류별 광물의 개수를 센다.
    # 광물의 개수를 기준으로 내림차순으로 정렬한다.
    counted = scan_minerals(minerals)

    # 정렬 방법에 따라 곡괭이의 개수를 줄여가며 피로도를 계산한다.
    answer = calculate_fatigue(counted, picks)
    return answer

def scan_minerals(minerals):
    i = 0
    counted = []
    flag = True
    while flag:
        target = []
        if i + 5 < len(minerals):
            target = minerals[i:i + 5]
        else:
            target = minerals[i:]
            flag = False
        dias, irons, stones = target.count('diamond'), target.count('iron'), target.count('stone')
        counted.append([dias, irons, stones])
        i += 5
    counted.sort(key=lambda _: (-_[0], -_[1]))
    return counted

def calculate_fatigue(counted, picks):
    result = 0
    for target in counted:
        if picks[0] > 0:
            picks[0] -= 1
            result += sum(target)
        elif picks[1] > 0:
            picks[1] -= 1
            result += target[0] * 5 + target[1] + target[2]
        elif picks[2] > 0:
            picks[2] -= 1
            result += target[0] * 25 + target[1] * 5 + target[2]
        else:
            break
    return result