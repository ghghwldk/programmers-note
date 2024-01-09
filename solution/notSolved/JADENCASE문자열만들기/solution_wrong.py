'''
JadenCase is a string where the first letter of every word is uppercase.
all other letters are lowercase

if the first letter is not an alphabet
the following letters can be written in lowercase letters
'''

# runtime error occured
def solution(s):
    # Numbers appear only as the first letter of a word.
    splitted = s.split(' ')
    l = []

    for sp in splitted:
        result = None
        if existsNumber(sp):
            result = sp.lower()
            l.append(result)
        else:
            if len(sp) > 1:
                result = sp[:1].upper() + sp[1:].lower()
            else:
                result = sp.upper()
            l.append(result)
    return ' '.join(l)

def makeResult(l):
    result = ''
    for i in range(len(l)-1):
        result = result + l[i] + ' '
    result = result + l[len(l)-1]
    return result

def existsNumber(s):
    first = s[0]
    if first.isalpha():
        return False
    else:
        return True