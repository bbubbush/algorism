'''
[ 짝수와 홀수 ]
evenOrOdd 메소드는 int형 num을 매개변수로 받습니다.
num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하도록 evenOrOdd에 코드를 작성해 보세요.
num은 0이상의 정수이며, num이 음수인 경우는 없습니다.

'''

'''
[ 접근방법 ]
num을 2로 나눈 나머지가 1이면 홀수, 0이면 짝수인 점에 착안하여 풀었다.
return값을 삼항식으로 했지만 그냥 if문으로 풀어도 충분하다.

'''

def evenOrOdd(num):
    return num % 2 == 0 and "Even" or "Odd"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))
