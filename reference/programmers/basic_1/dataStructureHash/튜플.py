def solution(s):
    result = []
    ls =  sorted([list(map(int, step1.split(','))) for step1 in s[2:-2].split('},{')], key=len)

    for l in ls:
        newItem = list(set(l) - set(result))[0]
        result.append(newItem)
    return result