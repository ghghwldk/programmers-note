# Hash를 활용
def solution(phone_book):
    # 번호 저장
    phone_hash = set(phone_book)
    for phone in phone_book:
        temp_num = ""
        # 앞 자리의 숫자부터 추가하면서, 저장된 번호가 있는지 확인
        for digit in phone:
            temp_num += digit
            if temp_num in phone_hash and temp_num!=phone:
                return False
    return True


'''
[정렬활용]
def solution(phone_book):
    answer = True
    # 문자열 정렬
    phone_book.sort()
    for i in range(len(phone_book)-1):
        # 같은 문자(숫자) 기준으로 정렬되었기 때문에, 앞 뒤만 비교
        if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
            answer = False
            break
    return answer
'''