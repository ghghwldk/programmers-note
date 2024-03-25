'''
숫자가 짝수인 경우, 항상 가장 마지막 비트는 0이다. 따라서 마지막 비트를 0에서 1로 바꿔준 값이 답이기 때문에 숫자+1 값을 answer에 넣어준다.
숫자가 홀수인 경우,
가장 뒤쪽에 있는 0을 1로 바꿔주고 그다음 비트를 0으로 바꿔주면 된다.
예를 들어 7(0111) 은 가장 뒤쪽에 있는 0을 1로 바꿔주고 그다음 비트를 0으로 바꿔준다. 즉, 11(1011)이 답이다.
그리고 9(1001) 은 1001 -> 1011 -> 1010 으로 10이 답이다.

'''
def solution(numbers):
    answer = []

    for number in numbers:
        if number % 2 == 0:
            answer.append(number + 1)
            continue

        number_bin = '0' + bin(number)[2:]
        number_bin = number_bin[:number_bin.rindex('0')] + '10' + number_bin[number_bin.rindex('0') + 2:]
        answer.append(int(number_bin, 2))

    return answer