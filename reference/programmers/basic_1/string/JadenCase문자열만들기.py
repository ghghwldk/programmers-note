'''
JadenCase is a string where the first letter of every word is uppercase.
all other letters are lowercase

if the first letter is not an alphabet
the following letters can be written in lowercase letters
'''
def solution(s):
    words = s.split(' ')
    jaden_case_words = []

    for word in words:
        if word[0].isalpha():
            jaden_case_words.append(word[0].upper() + word[1:].lower())
        else:
            jaden_case_words.append(word.lower())

    return ' '.join(jaden_case_words)

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