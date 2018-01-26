'''
[ 두 정수 사이의 합 ]
adder함수는 정수 a, b를 매개변수로 입력받습니다.
두 수와 두 수 사이에 있는 모든 정수를 더해서 리턴하도록 함수를 완성하세요. a와 b가 같은 경우는 둘 중 아무 수나 리턴하세요.
예를들어 a가 3, b가 5이면 12를 리턴하면 됩니다.

a, b는 음수나 0, 양수일 수 있으며 둘의 대소 관계도 정해져 있지 않습니다.

'''

'''
[ 접근방법 ]
처음에는 두 수의 대소관계를 설정해 min_value부터 max_value까지 for문을 돌려 풀었다.

하지만 a와 b의 차이가 무한이 큰 수라면 연산에 오랜 시간이 걸릴 것이다.
그래서 대한민국의 위대한 정규교육과정 속에서 배운 1~n까지 수의 합을 구하는 공식을 사용해 
for문 없이 풀어봤다.

다만 1부터 max_value까지의 합에서 1부터 min_value-1까지의 합을 빼는 것이라는 점을 주의해야 한다.

(다른사람의 풀이를 보니 절대값을 활용해 두 수의 거리만 구해 1부터 거리까지의 합을 구하는 분도 있어 놀랐다.)
'''
import sys
def adder(a, b):
    min_value = a < b and a or b
    max_value = a < b and b or a
    return max_value * (max_value+1) // 2 - (min_value-1) * min_value // 2


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(adder(3, 5))
print(adder(-3, -5))
print(adder(sys.maxsize, -sys.maxsize))