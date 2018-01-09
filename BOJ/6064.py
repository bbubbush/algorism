'''
[ 카잉 달력 ]
최근에 ICPC 탐사대는 남아메리카의 잉카 제국이 놀라운 문명을 지닌 카잉 제국을 토대로 하여 세워졌다는 사실을 발견했다.
카잉 제국의 백성들은 특이한 달력을 사용한 것으로 알려져 있다. 그들은 M 과 N 보다 작거나 같은 두 개의 자연수
x, y를 가지고 각 년도를 <x:y>와 같은 형식으로 표현하였다.
그들은 이 세상의 시초에 해당하는 첫 번째 해를 <1:1>로 표현하고, 두 번째 해를 <2:2>로 표현하였다.
<x:y>의 다음 해를 표현한 것을 <x':y'>이라고 하자. 만일 x < M 이면 x' = x + 1이고, 그렇지 않으면 x' = 1이다.
같은 방식으로 만일 y < N이면 y' = y + 1이고, 그렇지 않으면 y' = 1이다. <M:N>은 그들 달력의 마지막 해로서,
이 해에 세상의 종말이 도래한다는 예언이 전해 온다. 

예를 들어, M = 10 이고 N = 12라고 하자. 첫 번째 해는 <1:1>로 표현되고, 11 번째 해는 <1:11>로 표현된다.
<3:1>은 13 번째 해를 나타내고, <10:12>는 마지막인 60 번째 해를 나타낸다. 

네 개의 정수 M, N, x 와 y가 주어질 때,
<M:N>이 카잉 달력의 마지막 해라고 하면 <x:y>는 몇 번째 해를 나타내는 지를 구하는 프로그램을 작성하라. 

입력 예제)
3
10 12 3 9
10 12 7 2
13 11 5 6

출력 예제)
33
-1
83

'''

'''
[ 접근방법 ]
1차 시도 : 처음부터 끝까지 모든 경우를 구해놓고 해당 값이 있는지 찾느라 시간초과
2차 시도 : 2차원 배열을 만들어 x값에 따라 나오는 y값을 순차적으로 기록해서 메모리 초과
3차 시도 : 2차원배열을 다 날려버리고 x값에 다라 y값이 나오는 순차적 배열만 찾아서 공식으로 계산

이런 과정을 거쳐 풀었다.
m, n, x, y가 10, 12, 3, 9 일때

x값에 따라 y의 순차적인 값
x   [y1 y2  y3  y4  y5  y6]
1   [1  11  9   7   5   3]  
2   [2  12  10  8   6   4]
3   [3  1  11  9   7   5]
4   [4  2  12  10  8   6]
5   [5  3  1   11  9   7]
6   [6  4   2   12  10  8]   
7   [7  5   3   1   11  9]
8   [8  6   4   2   12  10]
9   [9  7   5   3   1   11]
10  [10 8   6   4   2   12]

이런 식으로 구해진다. 그럼 x와 y의 값이 x번째 배열의 y값의 순서를 알 수 있으면 해당 x,y의 값이
몇 번째 인지 알 수 있다.

예제인 x=3, y=9일때는 x가 3인 배열의 항목 중 9의 값이 몇번째인 보자 3, 1, 11를 거쳐 9가 등장한다.
즉, 4번째 등장하게 된다. 그러면 3번째 까지는 10번의 순서를 거치고 4번째 순서를 도는 과정 중에 3, 9가 등장하게 된다.

그래서 m * (인덱스-1) + x 의 값이 정답이 된다. (10 * (4-1) + 3) = 33

하지만 이렇게 푸니 m * n 만큼의 2차원 배열이 필요하게 된다.(위에 예제는 y7부터 y1의 값을 반복하기 때문에 절반만 표현했다.)
그래서 생각했다. 모든 배열을 다 저장하지 말고 x값에 해당하는 배열만 뽑자!  (이것도 결국 메모리초과가 되었다)

메모리를 줄이기 위해 식을 만지다 보니 결국은 변수 하나만 활용해서 풀게 되었다. 

~~끝~~

수식을 도출하기 까지 너무많은 시간이 필요했다. 오래 이 문제를 만지다보면 점점 본인만의 수식이 생기게 될 것이다.

'''

def caingCal(m, n, x, y):

    # 항상 m < n의 형태로 계산을 하기 위해 식을 조정
    # m, n, x, y = n, m, y, x 가 성립한다. 
    if m > n:
        m, n, x, y = n, m, y, x

    # x와 y의 값이 같은 경우 x 혹은 y 번째 값이 된다.
    if x == y:
        return x

    
    temp = x
    for i in range(1, n+1):
        val = temp + m - n
        
        if val < 1:
            val = n + val
            
        temp = val
        
        if temp == y:
            return m * i + x       

    return -1
        
for i in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(caingCal(m, n, x, y))


