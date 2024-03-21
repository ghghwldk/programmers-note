# i have to order the filename in numerical order.
def solution(files):
    # sorting the filename under the criterias give.
    converteds = [convert(files[i], i) for i in range(len(files))]
    sortedConverteds = sorted(converteds, key=lambda x: (x[0], x[1], x[2]))
    print('here-l', sortedConverteds)
    print('here-f', files)
    return [files[item[2]] for item in sortedConverteds]

def convert(fileName, idx):
    startNumber, endNumber = -1, -1
    findingStart = True
    for i in range(len(fileName)):
        if findingStart:
            if isNumber(fileName[i]):
                startNumber = i
                findingStart = False
        else:
            if not isNumber(fileName[i]):
                endNumber = i
                break
        if i == len(fileName) -1:
            endNumber = len(fileName) + 1
    return fileName[:startNumber].upper(), int(fileName[startNumber:endNumber]), idx


def isNumber(c):
    return c >= '0' and c <= '9'