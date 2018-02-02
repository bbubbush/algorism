'''
[ 검문 ]
트럭을 타고 이동하던 상근이는 경찰의 검문을 받게 되었다. 경찰은 상근이가 운반하던 화물을 하나하나 모두 확인할 것이기 때문에,
검문하는데 엄청나게 오랜 시간이 걸린다. 상근이는 시간을 떼우기 위해서 수학 게임을 하기로 했다.

먼저 근처에 보이는 숫자 N개를 종이에 적는다. 그 다음, 종이에 적은 수를 M으로 나누었을 때, 나머지가 모두 같게 되는 M을
모두 찾으려고 한다. M은 1보다 커야 한다. N개의 수가 주어졌을 때, 가능한 M을 모두 찾는 프로그램을 작성하시오.
    
입력 예제)
3        -> n
6
34
38

출력 예제)
2 4

'''
        
'''
[ 접근방법 ]
어렵다. 혼자서 풀어보다 도저히 못풀겠어서 검색했는데 그 설명을 이해하는데 반나절을 썻다. 풀이를 참고한 페이지는 맨 아래에 있다.

m의 값을 찾는 것이 목표다. m은 입력값 각각을 m으로 나누었을때 모두 같은 나머지(이하 r)을 같게 하는 수이다. 위의 예를 보자.

        6 = 4 * 1 + 2,        34 = 4 * 8 + 2,          38 = 4 * 9 + 2
    
2의 경우는 r이 모두 0으로 떨어지므로 설명을 생략했다. 4의 경우는 모두 r이 2가 된다.

이번엔 수식으로 보자. 입력된 값을 각각 x1, x2, ... xn이라고 할 때 m값을 갖는 x의 n번째 값은 xn = m * yn + r의 형태일 것이다.
예제를 대입해 보면 m = 4, r = 2이며 yn은 각각 1, 8, 9 이다.

그럼 m값은 어떻게 찾아야할까? 전혀 생각지도 못한 방법이었는데 입력된 값들의 차이를 이용하는 것이다. 현재 m을 안다고 가정할 때

        x1 = m * y1 + r,        x2 = m * y2 + r, ......

이 상태에서 x2-x1 = m(y2-y1)이 된다. r은 제거되고 m과 어떤 y값의 차의 곱이 된다. 이를 모든 입력값에 적용하면 n-1만큼의 길이를 갖는 배열이 탄생한다.

       distance_list = [m(y2-y1), m(y3-y2),..., m( yn - y(n-1) )]
        
이렇게 보니깐 특징이 보인다. 모두 m을 가지고 있다. 즉, 배열안의 모든 값에 영향을 끼치는 것은 m이다. 또한 모든 값에 대해 m은 약수가 된다. 그래서  
m의 최대값만 알 수 있다면 m의 약수 모두 m의 값에 들어 갈 수 있다. 어떤 약수든 자신의 짝과 곱하면 원래의 수가 되기 때문이다.

따라서 최대의 m값만 안다면 m에 들어 갈 수 있는 수는 m의 약수들 일 것이다. 공통된 약수의 최대값, 최대공약수(gcd)를 구해 최대공약수의 약수를 구하면 된다.

보충 설명을 위해 예제를 다시 살펴보자

input이 6, 34, 38일 때, distance_list = [28, 4] 이 된다. distance_list 전체의 gcd는 4이다. 다시 바꿔 말하면 4는 모든 값의 약수이며
4의 약수들 또한 모든 값에 대해 약수가 된다.

4의 약수인 1, 2, 4가 모두 답인데 주어진 문제에서 m > 1 란 조건이 있어 2, 4가 답이 된다.

혼자서 풀면 절대 못풀었을 문제이다. 많은 분들의 도움을 받아 겨우 이해하고 넘어갔다. 다시 한번 아래의 링크를 통해 감사를 표한다.

Ref : http://kthng.tistory.com/20
Ref : https://www.acmicpc.net/board/view/11630

'''

import math

def spot_check(n, number_list):
    distance_list = []

    # init distance_list
    for i in range(1, n):
        distance_list.append(number_list[i] - number_list[i-1])

    # get gcd
    gcd = distance_list[0]
    for distance in distance_list:
        gcd = math.gcd(gcd, distance)

    
    answer = []
    answer.append(gcd)
    for i in range(2, int(math.sqrt(gcd))+1):
        if gcd % i == 0:
            answer.append(i)
            if i != gcd//i:
                answer.append(gcd//i)
    
    answer.sort()
    return ' '.join(map(str, answer))

n = int(input())

number_list = []
for i in range(n):
    number_list.append(int(input()))

print(spot_check(n, number_list))

# https://github.com/bbubbush/algorithm/tree/master/BOJ/2981.py
