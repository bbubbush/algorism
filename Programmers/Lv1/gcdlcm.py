'''
[ 최대공약수와 최소공배수 ]
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환해주는 gcdlcm 함수를 완성해 보세요. 배열의 맨 앞에 최대공약수, 그 다음 최소공배수를 넣어 반환하면 됩니다. 
예를 들어 gcdlcm(3,12) 가 입력되면, [3, 12]를 반환해주면 됩니다.
'''

'''
[ 접근방법 ]
간단하지만 복잡할 수 있는 최대공약수(Greatest Common Divisor, 이하 gcd)와 최소공배수(Least Common Multiple, 이하 lcm)문제이다.

일단 우리가 배운 gcd와 lcm의 정의를 보자.

gcd : 자연수 a, b의 공통된 약수 중 가장 큰 수.
lcm : 자연수 a, b의 공통된 배수 중 가장 작은 수.

ex) a = 60, b = 48일 때, lcm과 gcd 구하기(정규교육 버전)

		a 		b
	2	|60		48
	2 	|30		24
	3 	|15		12
		5 		4 		<- 서로소 인 두 수 5, 4는 각각 a를 gcd로 나눈 몫, b를 gcd로 나눈 몫이라고 생각할 수 있다.

lcm의 경우, 학교에서 배운 내용은 두 자연수 a, b를 나란히 놓고 2부터 차근차근 무엇으로 둘다 나누어 떨어질까?
생각하면서 나온 몫을 더이상 공통된 약수가 나오지 않을 때까지 나누었다.
gcd는 공통된 약수들의 곱이고, lcm은 여기에 더해 서로 약수가 없는 나머지 수까지 곱했다.
이걸 다시 보니 '우리가 참 고등교육을 받고 자라왔구나' 라는 생각이 갑자기 든다 ㅎㅎ

다시 본론으로 가서 위의 식을 통해 gcd = 2 * 2 * 3, lcm = gcd * 5 * 4가 된다. 우리는 모두 이 사실을 배웠지만 기억을 못하는 것 뿐이다!
여기서 5와 4에 집중을 해보겠다. 5는 a를 gcd(12)로 나눈 몫이다. 그럼 a = gcd * 5라고도 할수 있지 않을까? 여기서 유클리드 호제법이 출발한다.

	a = gcd(a, b) * x, b = gcd(a, b) * y 	(단, x, y는 정수)

a * b = gcd * gcd * x * y란 식도 성립이 된다. 여기서 우항을 보면 gcd * x * y는 무엇인가? 바로 lcm이다 !! 즉, a * b = gcd * lcm이 된다.

따라서 우리는 gcd를 구하기만 하면 문제를 해결할 수 있다.

유클리드 호제법은 a, b (단, a < b)일 때 b % a == 0이면 gcd(a, b) = a이고, 0이 아닐 경우에는 b = a, a = b % a의 값이 들어가게 된다.
이를 반복하게 되어 a % b == 0이 될 때, a의 값은 gcd가 된다.

lcm은 a * b = gcd * lcm을 이용해서 lcm = a * b / gcd 이 된다.

아래 첫번째 코드는 위의 기능을 구현한 것이고, 두번째 코드는 내부함수 gcd를 사용하여 구한 것이다.

'''
from fractions import gcd

def gcdlcm(a, b):
	# 첫번째 방법
    # answer[0] = 제수, answer[1] = 피제수
    answer = a < b and [a, b] or [b, a]
    
    mod = answer[1] % answer[0]
    while(mod > 0):
        answer[1], answer[0] = answer[0], mod
        mod = answer[1] % answer[0]


    answer[1] = int(a * b / answer[0])
    return answer
    # 두번째 방법
    #return [gcd(a, b), int(a*b/gcd(a, b))]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(12, 3))
print(gcdlcm(58, 43))

# 참고 : https://opentutorials.org/module/1544/9533