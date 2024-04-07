def solution(phone_book):
    phone_book = sorted(phone_book)

    for i in range(len(phone_book)-1):
        current, after = phone_book[i], phone_book[i+1]

        if check접두어(current, after):
            # print(current, after)
            return False

    return True


def check접두어(current, after):
    splitted = after[:len(current)]
    is접두어 = False
    if current == splitted:
        is접두어 = True

    return is접두어

# ["119", "97674223", "1195524421"]	false
# ["123","456","789"]	true

print(solution(["119", "97674223", "1195524421"]))
# print(solution(["123","456","789"]))