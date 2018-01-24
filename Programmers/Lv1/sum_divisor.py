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


잘만 동작할 줄 알았던 세번째 코드가 의외의 곳에서 문제가 터졌다!! 

a. print(math.sqrt(8508977))					-> 2917.0150839514013
b. print(math.sqrt(8508977)**2)				-> 8508977.0 
c. print(0.0150839514013 * 0.0150839514013)	-> 0.00022752558987678025

무엇이 문제인지 쉽게 인지하기 힘들다.
a의 경우 8508977의 루트 값이다. 
b의 경우 8508977의 루트값에 제곱을 했다. 당연하다. 루트에 다시 제곱이니 본연의 값이 나와야 한다.
c의 경우가 문제다. a의 실수부 값만 가져와서 제곱을 했다. 

8508889

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
    
    print(sum(answer) + (math.sqrt(num)**2 == num and int(math.sqrt(num)) or 0))
    end_time = t.time()
    print('total_time : {}'.format(end_time-start_time))   
    print(math.sqrt(num).is_integer())
    return sum(answer) + (round(math.sqrt(num))**2 == num and int(math.sqrt(num)) or 0)



# 아래는 테스트로 출력해 보기 위한 코드입니다.
'''
print(sum_divisor(12))
print(sum_divisor(10000000))
print(sum_divisor(8508977))		# check point
print(sum_divisor(sys.maxsize))	# 2147483647
'''
print(0.1 * 3 == 0.3)
print(0.1 + 0.1 + 0.1 == 3)

print(10**2 + 0.1**2 == 10.1**2)