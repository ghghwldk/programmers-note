
def solution(cap, n, deliveries, pickups):
    '''
    가장 멀리 있는 곳의 배달은 어차피 끝내야한다.
    먼저 처리하자.
    '''
    deliveries = deliveries[::-1]
    pickups = pickups[::-1]
    answer = 0

    have_to_deli = 0
    have_to_pick = 0

    for i in range(n):
        have_to_deli += deliveries[i]
        have_to_pick += pickups[i]

        '''
        이때 각 위치의 배달/픽업 값들에서 cap값을 빼준다. 
        이 연산의 결과들이 모두 음수라면 해당 위치의 배달/픽업 값이 한번에 실어 나를 수 있는 용량(=cap)보다 적은 것이다. 
        오가는 길에 겸사겸사 추가적으로 배달/픽업이 가능하다는 의미이다!

        때문에 have_to_deli, have_to_pick 값이 양수가 되기 전까진 이동이 필요 없.
        이 두 값 중 하나라도 양수가 될 때만 해당 위치로 이동해주면 된다.
        '''
        while have_to_deli > 0 or have_to_pick > 0:
            have_to_deli -= cap
            have_to_pick -= cap
            # 어차피 한번 가면 다시 물류창고로 되돌아와야 하므로 정답에는 거리 x 2를 더해준다.
            answer += (n - i) * 2

    return answer