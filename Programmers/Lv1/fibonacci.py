'''
[ 피보나치 수 ]
피보나치 수는 F(0) = 0, F(1) = 1일 때, 2 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 점화식입니다. 
2 이상의 n이 입력되었을 때, fibonacci 함수를 제작하여 n번째 피보나치 수를 반환해 주세요. 
예를 들어 n = 3이라면 2를 반환해주면 됩니다.
'''
'''
[ 접근방법 ]
일반적인 피보나치로 풀면 자꾸 시간초과가 떠서 메모이제이션을 사용해서 시간을 단축시켰다.

BOJ에서도 비슷한 문제를 풀어서 별다른 설명없이 넘어가겠다.

'''

listA = [0, 1]
def fibonacci(num):
    if len(listA) > num: return listA[num]
    #if num < 2: return listA[num]
    listA.append(fibonacci(num-1) + fibonacci(num-2))
    
    return listA[num]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(fibonacci(3))