'''
괄호개수는 맞지만 짝이 맞지 않은 형태로 작성되어 오류 발생
>> 올바른 순서대로 배치된 괄호 문자열을 알려주는 프로그램 개발

균형잡힌 괄호 문자열
좌우 개수 같을 때

올바른 괄호 문자열
짝도 모두 같을 때

균형잡힌 괄호 문자열일 때 올바른 괄호 문자열로 변환가능
'''
# p: 균형잡힌 괄호 문자열
def solution(p):
    # answer = ''



    # print(is올바른괄호문자열('())('))
    # print(두균현잡힌문자열로분리('(())()'))
    # 올바른 괄호 문자열로 변환한 결과
    # return answer
    return convert(p)
def convert(before):
    if before == '':
        return ''
    u, v = 두균형잡힌문자열로분리(before)
    if is올바른괄호문자열(u):
        return u + convert(v)
    # 4
    else:
        s = '(' + convert(v) + ')'
        u = u[1: -1]
        u = 괄호반대로변경(u)
        return s+ u

def 괄호반대로변경(before):
    after = ''
    for c in before:
        if c== '(':
            after += ')'
        else:
            after += '('
    return after

def 두균형잡힌문자열로분리(before):
    left, right = 0, 0
    for c in before:
        if c == '(':
            left += 1
        else:
            right += 1
        if left == right:
            break
    return before[:left+ right], before[left+right:]


def is올바른괄호문자열(s):
    스 = []
    result = True
    for c in s:
        if c == '(':
            스.append(c)
        else:
            if not 스:
                result = False
                break
            스.pop()
    return result

def to스택(s):
    result = []
    for c in s:
        result.append(result)
    return result
'''
"(()())()"	"(()())()"
")("	"()"
"()))((()"	"()(())()"
'''
print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))