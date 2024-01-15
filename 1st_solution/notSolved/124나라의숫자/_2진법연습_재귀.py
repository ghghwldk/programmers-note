def ejin(num, current):
    # this method is for the recursive action
    # i have to define the condition for the excape in the beginning of the method.
    if num == 0:
        return current

    divided = int(num // 2)

    return ejin(divided, str(int(num % 2)) + current)

initialResult = ''
print(ejin(10, initialResult))