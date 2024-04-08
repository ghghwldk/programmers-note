

def initDict():
    d = dict()
    for i in range(ord('A'), ord('Z')+1):
        # print(chr(i))
        d[chr(i)] = i - 64
    return d

def get가장긴(d, remain):
    가장긴 = ''
    for i in range(1, len(remain)+1):
        splitted = remain[:i]
        if splitted in d.keys():
            가장긴 = splitted
        else:
            break
    return 가장긴

'''
무손실 알고리즘
압축 전의 정보를 완벽하게 복원 가능
>> LZW 알고리즘

LZW 압축은 다음 과정을 거친다.

1. 길이가 1인 모든 단어를 포함하도록 사전을 초기화한다.
2. 사전에서 현재 입력과 일치하는 가장 긴 문자열 w를 찾는다.
3. w에 해당하는 사전의 색인 번호를 출력하고, 입력에서 w를 제거한다.
4. 입력에서 처리되지 않은 다음 글자가 남아있다면(c), w+c에 해당하는 단어를 사전에 등록한다.
5. 단계 2로 돌아간다.
'''
def solution(msg):
    answer = []
    d = initDict()
    count = len(d)

    while True:
        # 2
        w = get가장긴(d, msg)
        # 3
        answer.append(d[w])
        msg = msg[len(w):]
        # 4
        if len(msg) == 0:
            break
        else:
            count+=1
            d[w + msg[0]] = count

    # 현재입력을 구한다.
    # 다음글자를 구한다.
    # 다음글자를 사전에 추가한다.
    # 현재입력에 대한 출력을 answer에 추가한다.
    return answer
# msg = 'KAKAO'
msg = 'TOBEORNOTTOBEORTOBEORNOT'
# msg = 'ABABABABABABABAB'
print(solution(msg))
'''
KAKAO	[11, 1, 27, 15]
TOBEORNOTTOBEORTOBEORNOT	[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
ABABABABABABABAB	[1, 2, 27, 29, 28, 31, 30]
'''