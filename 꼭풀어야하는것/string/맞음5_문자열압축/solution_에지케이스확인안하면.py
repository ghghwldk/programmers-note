def 이전것처리(before, count):
    after = ''
    if count == 1:
        after = before
    else:
        after = str(count) + before
    return after

def solution(s):
    minLen = 1e9
    maxLen = len(s) // 2
    '''
    엣지케이스 확인해야함
    '''
    # if len(s) == 1:
    #     return 1
    for length in range(1, maxLen+1):
        start, end = 0, length
        before = None
        count = 0
        result = ''
        while True:
            if end > len(s):
                result = result + 이전것처리(before, count)
                result = result + s[start:]
                break
            # print('se', start, end)
            splitted = s[start:end]
            if before == None:
                count += 1
            elif splitted == before:
                count += 1
            else:
                result = result + 이전것처리(before, count)
                count = 1

            before = splitted # 자른 것과 동일유무에 상관없이 before를 갱신한다. 다음 자른 것과의 비교를 위해서이다.

            start += length
            end += length
        # print(length, result)
        if minLen > len(result):
            minLen = len(result)
            # print(result)

    return minLen


# s = "aabbaccc"
# s = "ababcdcdababcdcd"
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
s = '1'
print(solution(s))