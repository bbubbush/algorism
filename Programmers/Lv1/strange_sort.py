'''
[ 문자열 내 마음대로 정렬하기 ]
strange_sort함수는 strings와 n이라는 매개변수를 받아들입니다.
strings는 문자열로 구성된 리스트인데, 각 문자열을 인덱스 n인 글자를 기준으로 정렬하면 됩니다.

예를들어 strings가
[sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1인 문자 u, e ,a를 기준으로 정렬해야 하므로
결과는 [car, bed, sun]이 됩니다.
strange_sort함수를 완성해 보세요.

'''

'''
[ 접근방법 ]
처음에는 해당 인덱스의 값을 맨 앞으로 빼서 비교했다. 위에서 예를 든 sun을 uns로 변환하여
비교한 것이다. 하지만 채점프로그램이 n번째 글자가 같으면 n+1의 값을 비교하는것이 아니라
원형인 0번째 인덱스를 비교하는 것이다. 그래서 n번째 인덱스의 값을 원형에 더해 usun 처럼
만들었다.
비교 후에 정렬을 하고 원형으로 돌려논 뒤에 출력했다.

'''


def strange_sort(strings, n):
    """ 정렬 기준이 같을 때는 리스트 순으로 반영해야해서 이건 실패
    temp = sorted(list(map(lambda x : x[n:]+x[:n], strings)))
    return list(map(lambda x : x[-n:]+x[:-n], temp))
    """
    return list(map(lambda x : x[1:], sorted(list(map(lambda x : x[n]+x, strings)))))


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( strange_sort(["sun", "bed", "car"], 1) )
