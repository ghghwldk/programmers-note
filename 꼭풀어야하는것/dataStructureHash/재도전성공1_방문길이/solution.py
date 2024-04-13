'''
게임 캐릭터는 4가지 명령어를 통해 이동
시작은 0,0
경계에서도 이동가능

처음 걸어본 길이를 구하려고 한다.
좌표평면의 경계를 넘어가는 명령어는 무시
'''

# dir: 명령어
def solution(dirs):
    dLocation = {'U': (-1, 0), 'D': (1, 0), 'R': (0,1), 'L': (0,-1)}
    r, c = 0, 0
    lineHashSet = set()
    for dir in dirs:
        dr, dc = dLocation[dir]
        nr, nc = r + dr, c + dc

        if nr < -5 or nr > 5 or nc < -5 or nc > 5:
            continue
        lineHash = getLineHash((r, c), (nr, nc))
        # print(lineHash)
        lineHashSet.add(lineHash)
        r, c = nr, nc
    return len(lineHashSet)


def getLineHash(p1, p2):
    hash1, hash2 = getHash(p1), getHash(p2)
    return max(hash1, hash2) * 10000 + min(hash1, hash2)

def getHash(point):
    r, c = point
    return 1000 * r + c

print('answer: ', solution("LULLLLLLU"))
'''dirs	answer
"ULURRDLLU"	7
"LULLLLLLU"	7'''