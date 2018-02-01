'''
[ 최소공배수 ]
두 자연수 A와 B에 대해서, A의 배수이면서 B의 배수인 자연수를 A와 B의 공배수라고 한다.
이런 공배수 중에서 가장 작은 수를 최소공배수라고 한다.
예를 들어, 6과 15의 공배수는 30, 60, 90등이 있으며, 최소 공배수는 30이다.

두 자연수 A와 B가 주어졌을 때, A와 B의 최소공배수를 구하는 프로그램을 작성하시오.
               
입력 예제)
3            -> Test case
1 45000
6 10
13 17

출력 예제)
45000
30
221

'''
        
'''
[ 접근방법 ]
최대공약수(gcd)와 최소공배수(lcm)는 알고리즘에 있어 빠지지 않는 단골문제이다. 항상 gcd이 우선 되어야 lcm을 구할 수 있다.

두 수 m, n의 gcd는 유클리드호제법(혹은 math lib)으로 구할 수 있고, lcm은 m*n//gcd로 구할 수 있다.

programmers 알고리즘 문제를 풀다 비슷한 문제를 만나 작성한 코드가 있다.

https://github.com/bbubbush/algorithm/blob/master/Programmers/Lv1/gcdlcm.py     이걸 보면 조금 더 자세한 설명이 되어있다.

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
    
    


# test case    
for t in range(int(input())):
    m, n = map(int, input().split())
    print(lcm(m, n))
