import math
from collections import defaultdict

answer = []
table = defaultdict(list)

def solution(fees, records):
    convert(fees, records)
    appendLastExit()
    getAnswer(fees, table)

    return answer

def convert(fees, records):
    global table

    for i in range(len(records)):
        time, number, state = records[i].split()
        minutes = int(time[:2]) * 60 + int(time[3:])
        table[number].append(minutes)

def appendLastExit():
    global table

    for i in table:
        if(len(table[i])%2 == 1):
            table[i].append(23*60 + 59)


def getAnswer(fees, table):
    global answer
    cars = sorted(table.keys())

    baseTime, baseFee, unitTime, unitFee = fees[0], fees[1], fees[2], fees[3]
    for c in cars:
        money = 0
        time = sum(table[c][1::2]) - sum(table[c][::2])
        if time > baseTime:
            money += baseFee + math.ceil((time-baseTime) / unitTime) * unitFee
        else:
            money += baseFee

        answer.append(money)