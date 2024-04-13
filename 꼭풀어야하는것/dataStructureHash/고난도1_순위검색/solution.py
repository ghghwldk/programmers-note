def binary_search(arr, start, end, target): # lower_bound
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] >= target:
            end = mid
        else:
            start = mid + 1
    return start

def solution(infos, queries):
    answer = []
    # 모든 케이스들 초기화
    cases = {}
    for lan in ['cpp', 'java', 'python', '-']:
        for job in ['backend', 'frontend', '-']:
            for career in ['junior', 'senior', '-']:
                for food in ['chicken', 'pizza', '-']:
                    cases[lan+' '+job+' '+career+' '+food] = []

    # info로 가능한 케이스들에 점수 추가
    for info in infos:
        info = info.split()
        for lan in [info[0], '-']:
            for job in [info[1], '-']:
                for career in [info[2], '-']:
                    for food in [info[3], '-']:
                        cases[lan+' '+job+' '+career+' '+food].append(int(info[4]))

    # 각 케이스 별 점수 오름차순 정리
    for k in cases.keys():
        cases[k].sort()

    # 쿼리에서 나오는 케이스들에 가능한 갯수 구하기
    for query in queries:
        query = query.split(' and ')
        query[3], score = query[3].split()
        scores = cases[query[0]+' '+query[1]+' '+query[2]+' '+query[3]]
        answer.append(len(scores)-binary_search(scores, 0, len(scores), int(score)))
    return answer