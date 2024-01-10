# i have to order the filename in numerical order.
def solution(files):
    s = 's12'
    print(s[2:])

    # sorting the filename under the criterias give.
    l = [f(files[i], i) for i in range(len(files))]
    l = sorted(l, key=lambda x: (x[0], x[1], x[2]))
    print(l)
    return [files[item[2]] for item in l]

def f(fn, idx):
    startNumber, endNumber = -1, -1
    findingStart = True
    for i in range(len(fn)):
        if findingStart:
            if isNumber(fn[i]):
                startNumber = i
                findingStart = False
        else:
            if not isNumber(fn[i]):
                endNumber = i
                break
        if i == len(fn) -1:
            endNumber = len(fn) + 1
    return fn[:startNumber].upper(), int(fn[startNumber:endNumber]), idx


def isNumber(c):
    return c >= '0' and c <= '9'