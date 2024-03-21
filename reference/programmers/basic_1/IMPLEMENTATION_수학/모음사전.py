'''
[규칙을 활용한 풀이]

[781, 156, 31, 6, 1] : 'A-E', 'E-I' 처럼 순서가 1만 차이날 경우, 경우의 수를 계산한 것이다.

1: 맨 뒷자리만 다른 경우
1 = 1

6 : 뒤에서 두번째 자리가 다른 경우 → 두번째 자리에서 1 차이나고(+1), 뒷 자리가 다른 경우 * 5
5 * 1(나머지 자리) + 1(현재 자리) = 6

31 : 뒤에서 3번째 자리가 다른 경우 → 세번째 자리에서 1 차이나고(+1), 나머지 자리가 다른 경우 * 5
6 * 5(나머지 자리) + 1(현재 자리)  = 31 

이를 재귀적으로 반복하면 나머지 성분도 구할 수 있다.
출처: https://only-wanna.tistory.com/entry/Python-프로그래머스-모음사전-풀이 [싶만생각:티스토리]
'''

def solution(word):
    answer = 0
    arr = ['A', 'E', 'I', 'O', 'U']
    num = [781, 156, 31, 6, 1]

    for i in range(len(word)):
        answer += arr.index(word[i]) * num[i] + 1

    return answer