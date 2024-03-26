from collections import defaultdict

def 올림(before):
    return int(before) + 1 if before - int(before) > 0 else int(before)

기본시간분, 기본요금원, 단위시간분, 단위요금원 = None, None, None, None
def 시간기준요금구하기(spanned):
    if spanned <= 기본시간분:
        return 기본요금원
    else:
        초과시간 = spanned - 기본시간분
        return 기본요금원 + (올림(초과시간 / 단위시간분) * 단위요금원)


def solution(fees, records):
    global 기본시간분, 기본요금원, 단위시간분, 단위요금원
    기본시간분, 기본요금원, 단위시간분, 단위요금원 = fees


    # print('--previous records', records)
    converteds = []
    for record in records:
        시간, 차넘버, 인아웃 = record.split(' ')
        converteds.append((convertTime(시간), 차넘버, 인아웃))
    # print('--converted records', converteds)
    # get perVehicle
    perVehicle = defaultdict(list)
    for converted in converteds:
        시간, 차넘버, 인아웃 = converted
        perVehicle[차넘버].append((시간, 인아웃))
    # 출차기록 없으면, 더해주기
    for 차넘버 in perVehicle.keys():
        l = perVehicle[차넘버]
        if not len(l) % 2 ==0:
            l.append((23* 60 + 59, 'OUT'))
    # print(perVehicle)
    # 차넘버별 주차시간 구하기
    timePerCarNums = defaultdict(int)
    for 차넘버 in perVehicle.keys():
        time = 0
        l = perVehicle[차넘버]
        # print('ff', l)
        for i in range(0, len(l), 2):
            입장시간, 인아웃 = l[i]
            퇴장시간, 인아웃 = l[i+1]
            time += (퇴장시간 - 입장시간)
        # timePerVehicle[차넘버] = time
        timePerCarNums[int(차넘버)] = time
    # print('--before')
    # print(timePerCarNums)
    # print('--after')
    # timePerCarNums = sorted(timePerCarNums)
    차넘버로정렬된소요시간 = [timePerCarNums[carNum] for carNum in sorted(timePerCarNums)]
    return [시간기준요금구하기(소요시간) for 소요시간 in 차넘버로정렬된소요시간]



def convertTime(before):
    time, minute = map(int, before.split(':'))
    return time * 60 + minute