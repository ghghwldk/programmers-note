def ejin(num):
    result = ''
    while num > 0:
        current = num % 2
        result = str(current) + result
        num = int(num / 2)
    return result
