'''
[ 약수의 합 ]
어떤 수를 입력받아 그 수의 약수를 모두 더한 수 sum_divisor 함수를 완성해 보세요. 
예를 들어 12가 입력된다면 12의 약수는 [1, 2, 3, 4, 6, 12]가 되고, 총 합은 28이 되므로 28을 반환해 주면 됩니다.
'''

'''
[ 접근방법 ]
1. 첫번째 코드
	제일 처음 풀었던 방식이다. 한 줄로 돌리는 for문이 낯설어 if문을 사용하기 위해 filter를 끌어다 쓴 코드이다.

2. 두번째 코드
	다른사람들의 풀이를 참고하여 num//2 까지만 for문의 범위를 좁혔다. 더 나아가 한 줄 for문 안에 if문이 들어가 깔끔해졌다.

3. 세번째 코드
	두번째 코드에서 더 나아가 sqrt(num)까지만 구하는 코드를 만들었다. 약수의 총합을 구하는거라 일일이 약수를 list에 담지 않았다.
    핵심은 sqrt(num) + 1까지는 짝으로 구하고, sqrt(num)의 실수부가 .0이면 num의 루트값이 정수이므로 약수에 포함이 된다.
    이를 통해 코드속도를 비약적으로 증가시켰다.

그럼 세번째 코드의 약수를 구하는 방법을 잠깐 설명하겠다.

예를 들어 100의 약수를 보자.
[1, 2, 4, 5, 10, 20, 25, 50, 100]

1, 2, 4, 5의 경우 쉽게 100의 약수임을 알수있다. 
그럼 100 % (1 or 2 or 4 or 5) == 0 을 성립하게 된다.
그렇다면 100 / (1 or 2 or 4 or 5) 를 해서 나온 (100, 50, 25, 20)은 100의 약수인가? 맞다. 약수 맞다.
이를 이용하면 5까지만 조사하면 100의 약수 9개 중 8개를 찾을 수 있다! 문제는 10이다. 10은 자신을 곱하여 100이 된다.

위의 규칙의 활용하면 크게 둘로 나누어 약수를 구하게 된다.
1) 1부터 sqrt(num)-1까지 약수를 쌍으로 찾기.
2) sqrt(num)이 정수이면 약수가 된다.(약수는 정수만 가능하다. 소수점 값이 있거나, 복소수는 취급하면 안된다)

이런 과정을 100의 약수에 대입해보면
1) 1부터 sqrt(100)-1까지 약수를 쌍으로 찾는다. [1, 2, 4, 5, 20, 25, 50, 100]
2) sqrt(100)이 정수이면 약수로 판단한다. sqrt(100)은 10.0이기 때문에 10이 100의 약수가 된다.

아래의 코드는 각각의 방법을 프로파일링했다.

코드설명은 끝이고 이번 풀이과정을 기술하는 동안 알게된 사실을 함꼐 나누고 싶다.

print(0.1 * 3 == 0.3)

위의 값은 False다. 충분히 고민해보고 답이 생각 안나면 검색해보길 바란다.

'''
import math
import time as t
import sys

def sum_divisor(num):
    
    # 첫번째 코드
    start_time = t.time()
    print(sum(list(filter(lambda x : num % x == 0, list((i for i in range(1, num+1)))))))
    end_time = t.time()
    print('total_time : {}'.format(end_time-start_time))
    
    # 두번째 코드
    start_time = t.time()
    print(sum([i for i in range(1, num//2 + 1) if num % i == 0], num))
    end_time = t.time()
    print('total_time : {}'.format(end_time-start_time))   
    
    
    # 세번째 코드
    start_time = t.time()
    answer = []
    for i in range(1, round(math.sqrt(num)+0.5) ):
        if num % i == 0:
    	    answer.append(i + num//i)
    
    print(sum(answer) + (math.sqrt(num) % 1 == 0 and int(math.sqrt(num)) or 0))
    end_time = t.time()
    print('total_time : {}'.format(end_time-start_time))   
    return sum(answer) + (math.sqrt(num) % 1 == 0 and int(math.sqrt(num)) or 0)



# 아래는 테스트로 출력해 보기 위한 코드입니다.
#print(sum_divisor(12))
print(sum_divisor(8508977))
#print(sum_divisor(10000000))
#print(sum_divisor(sys.maxsize))	# 2147483647


