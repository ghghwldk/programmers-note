'''
[Time Complexity Analysis - After unsatifying time limitation of the problem]
The 'execute' function calls itself recursively and makes modifications
to the string in each call. In the worst case, it may create a recursive call
for each character in the original string, resulting in a total time complexity
of O(N^2), where n is the length of the original string.
'''

import sys
sys.setrecursionlimit(10**6)

def solution(s):
    if len(s) % 2 == 1:
        return 0
    return 1 if not execute(s, 0) == -1 else 0


def execute(s, count):
    # condition to exit recursive method
    if len(s) == 0:
        return count
    first = check(s)
    # impossible to make empty string
    if first == -1:
        count = -1
        return count
    return execute(s[:first]+ s[first+2:], count + 1)


# this method for checking existence of consecutive two letters in the string
def check(s):
    for i in range(len(s)-1):
        first, second = i, i+1
        if s[first] == s[second]:
            return first

    # return -1 if there is no consective two letters
    return -1
