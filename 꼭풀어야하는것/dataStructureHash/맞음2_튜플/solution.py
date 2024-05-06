def solution(s):
    # 앞 뒤 필요 없는 괄호 제거
    s = s[2: -2]
    # 배열 얻기
    ls = [list(map(int, temp.split(','))) for temp in s.split('},{')]
    ls = sorted(ls, key = len)


    result = []

    for i, l in enumerate(ls):
        currentSet = set(ls[i])
        '''
        집합연산은 많이 드는 작업이다.
        하지만, 이 경우에는 원소의 차집합을 구하기 위해 사용할 수 밖에 없다.
        '''
        difference = list(currentSet - set(result))[0]

        result.append(difference)

    return result