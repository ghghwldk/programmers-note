# 원소 추가
# 원소 존재 확인
'''
리스트에서의 x in s 연산의 평균 시간 복잡도 : O(n)
세트에서의 x in s 연산의 평균 시간 복잡도 : O(1)
'''

s = set()
s.add(1)
s.add(2)
print(1 in s)

'''
세트가 효율적인 이유 = 해시 테이블
세트의 x in s 연산의 평균 시간 복잡도가 O(1)이 될 수 있는 이유는 간단하다.
파이썬에서는 세트가 해시 테이블(hash table)로 구현되어 있기 때문이다.

해시 테이블을 이해하려면 우선 해시 함수를 이해해야 한다.
해시 함수는 임의의 데이터를 인자로 받아, 특정 범위 내의 데이터로 반환하는 함수다.
예를 들어, h(x) = x % 100이라는 함수가 있다면, 어떤 정수가 인자로 들어오더라도 0~99 사이의 숫자를 반환하게 된다.

해시 테이블은 해시 함수를 통해 데이터를 저장하는 자료구조다.
해시 함수를 통해 해싱한 후 나온 결과값을 배열의 인덱스로 사용하여, 해당 위치에 데이터를 저장하는 방식이다.
'''