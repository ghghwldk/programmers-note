'''
boundaries exist
'''

def solution(dirs):
    answer = 0

    dAndGo = {'U': (-1,0), 'D':(1,0), 'R': (0,1), 'L': (0,-1)}
    s = set()
    r, c = 0, 0
    for d in dirs:
        go = dAndGo[d]
        nr, nc = r + go[0], c + go[1]
        # go beyond the boundaries of the coordinate plane are ignored.
        if nr < -5 or nr > 5 or nc > 5 or nc < -5:
            continue
        s.add((nr, nc, r, c))
        s.add((r , c, nr, nc))

        # go to next location
        r, c = nr, nc

    # find the length of the path the game character first walked.
    return len(s) // 2