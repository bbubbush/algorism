'''
[ N개의 최소공배수 ]
두 수의 최소공배수(Least Common Multiple)란 입력된 두 수의 배수 중 공통이 되는
가장 작은 숫자를 의미합니다. 예를 들어 2와 7의 최소공배수는 14가 됩니다.
정의를 확장해서, n개의 수의 최소공배수는 n 개의 수들의 배수 중 공통이 되는
가장 작은 숫자가 됩니다. nlcm 함수를 통해 n개의 숫자가 입력되었을 때,
최소공배수를 반환해 주세요.
예를들어 [2,6,8,14] 가 입력된다면 168을 반환해 주면 됩니다.
'''

'''
[ 접근방법 ]
입력받은 N개의 숫자는 순서대로 소인수분해 하여 임시변수 tempDic에 담는다.
그 후 해당 지수의 가장 큰 차수를 찾기 위해 answer에 담긴 지수와 tempDic에
담긴 지수를 비교해 차수가 높은 것을 answer에 담는다
마지막으로 answer에 담긴 지수를 각각의 차수만큼 곱한 값을 모두 곱해 리턴한다
'''

# 머리가 나빠 손이 고생한 경우
import math

def nlcm(num):
    answer = {} # 모든 수의 소인수 분해 값중 차수가 가장 높은 값만 저장

    for i in num:
        n = i
        j = 2
        tempDic = {}
        while j < math.sqrt(n) + 1: # 소인수 분해
            if n % j is 0:
                if j in tempDic:
                    tempDic[j] += 1
                else:
                    tempDic[j] = 1
                n = n // j
                j = 2
            else:
                j += 1
                
        if n in tempDic:
            tempDic[n] += 1
        else:
            tempDic[n] = 1

        keys = tempDic.keys()

        for k in keys:
            if k in answer:
                answer[k] = max(tempDic[k], answer[k])
            else:
                answer[k] = tempDic[k]
    result = 1
    for i in answer.keys():
        result *= i ** answer[i]
    
    return result 

print(nlcm([2,6,8,14]));


# 참고할만한 좋은 풀이 방법
'''
[ 접근방법 ]
두 수 A, B의 최소공배수를 l, 최대공약수를 g라고 할 때
        A * B = l * g
라는 공식을 이용한 방법
우리가 원하는 값은 l이므로 l에 대한 수식으로 정리하면
        ㅣ = A * B / G가 된다
무엇보다 g값을 구하는 함수가 fractions에 내장되어 있어서 좋다
'''
from fractions import gcd

def nlcm(num):      
    answer = num[0]
    for n in num:
        answer = n * answer / gcd(n, answer)

    return answer

print(nlcm([2,6,8,14]));
