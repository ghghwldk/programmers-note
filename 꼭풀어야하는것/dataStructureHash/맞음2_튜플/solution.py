def solution(s):
    # 앞 뒤 필요 없는 괄호 제거
    s = s[2: -2]
    # 배열 얻기
    ls = [list(map(int, temp.split(','))) for temp in s.split('},{')]
    ls = sorted(ls, key = len)


    result = []

    for i, l in enumerate(ls):
        currentSet = set(ls[i])
        difference = list(currentSet - set(result))[0]

        result.append(difference)

    return result