'''
[ 최소공배수 ]
정수 A는 정수 B를 0보다 큰 정수인 N회 곱해 A를 구할 수 있다면 A는 B의 배수이다.

예:

    10은 5의 배수이다 (5*2 = 10)
    10은 10의 배수이다(10*1 = 10)
    6은 1의 배수이다(1*6 = 6)
    20은 1, 2, 4,5,10,20의 배수이다.
    
다른 예:

    2와 5의 최소공배수는 10이고, 그 이유는 2와 5보다 작은 공배수가 없기 때문이다.
    10과 20의 최소공배수는 20이다.
    5와 3의 최소공배수는 15이다.
    
당신은 두 수에 대하여 최소공배수를 구하는 프로그램을 작성 하는 것이 목표이다.

한 줄에 두 정수 A와 B가 공백으로 분리되어 주어진다.

50%의 입력 중 A와 B는 1000(103)보다 작다. 다른 50%의 입력은 1000보다 크고 100000000(108)보다 작다.

입력 예제)
121 199

출력 예제)
24079

'''
        
'''
[ 접근방법 ]
아마 while을 통해 2부터 나누는 방식(처음 정규교육에서 배우는 방식)으로 풀지 않기를 바라며 제출한 문제인 것 같다.
큰수의 입력은 위와같은 방식에 많은 제약이 있을 것이다. 하지만 우리의 유클리드호제법을 사용하면 짧은 시간내에 해결할 수 있다.

자세한 설명은 비슷한 문제를 풀며 적어둔 주석이 있다. 아래의 주소를 참고하면 좋겠다.

https://github.com/bbubbush/algorithm/blob/master/Programmers/Lv1/gcdlcm.py

'''
import math

def lcm(m, n):
    # case1 : use math lib
    '''
    return m * n // math.gcd(m, n)
    '''
    
    # case2 : Euclidean algorithm
    multiply_m_n = m * n
    if m > n:
        m, n = n, m
    answer = 0
    temp =  n % m 
    while temp > 0:
        m, n = temp, m
        temp = n % m

    return multiply_m_n // m

m, n = map(int, input().split())
print(lcm(m, n))
