'''
who're not my friends
virtual nickname rather than your original nickname

administrator window
watch various people in and out

# 2way to change nickname in a chat room
1. leaving and re-enter with a new nickname
2. change nickname in the chat room.

duplicate nicknames
'''
def makeResult(datas, nicksPerUserId):
    result = []
    for data in datas:
        result.append(nicksPerUserId[data[1]] + data[0])
    return result

def solution(record):
    #(message, userId)
    datas = list() # postfix, userId
    nicksPerUserId = dict() # {userId: nick}
    for r in record:
        splitted = r.split(' ')
        # process, userId, nickName = splitted[0], splitted[1], splitted[2]
        process, userId = splitted[0], splitted[1],


        if process == 'Enter':

            datas.append(('님이 들어왔습니다.', userId))
        elif process == 'Leave':
            datas.append(('님이 나갔습니다.', userId))
        # elif process == 'Change':
        #     data.append((''))
        if process == 'Enter' or process == 'Change':
            nickName = splitted[2]
            nicksPerUserId[userId] = nickName
    return makeResult(datas, nicksPerUserId)


