'''
[ 스택 수열 ]
스택 (stack)은 기본적인 자료구조 중 하나로, 컴퓨터 프로그램을 작성할 때 자주 이용되는 개념이다.
스택은 자료를 넣는 (push) 입구와 자료를 뽑는 (pop) 입구가 같아 제일 먼저 들어간 자료가
제일 나중에 나오는 (FILO, first in last out) 특성을 가지고 있다.

1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열을 만들 수 있다.
이 때, 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 하자.
임의의 수열이 주어졌을 때 스택을 이용해 그 수열을 만들 수 있는지 없는지,
있다면 어떤 순서로 push와 pop 연산을 수행해야 하는지를 알아낼 수 있다. 이를 계산하는 프로그램을 작성하라.

입력 예제)
8    -> n
4    -> 수열[0]
3
6
8
7
5
2
1    -> 수열[n-1]

출력 예제)
+
+
+
+
-
-
+
+
-
+
+
-
-
-
-
-

'''

'''
[ 접근방법 ]
일단 만든 코드가 자꾸 시간초과가 걸려 다른분의 코드와 무엇이 다른가 비교해보다 '차이가 없는데 왜 이코드는 될까?'라는 
심정으로 그분의 코드를 복붙해서 돌린결과 그냥 맞아버렸다... 다른분 코드를 퍼오면 주석처리를 해놓는데 미쳐 못해서 여기에
주소를 적어두겠다. 맛동산님 블로그 : http://tastydarr.tistory.com/160

문제의 풀이는 어렵지 않는데... 파이썬에서 편의를 위해 제공하는 함수를 함수로 쓰면 안된다는 것을 다시 한번 느끼며 최호성님의
C 강의가 절실히 간절했던 시간이었다.
처음에 if문 조건을 if in_data_list[idx] in temp_s: 이렇게 주었다. 스택안에 값이 있는 경우를 편하게 적기 위해 'in'을 썻는데
이게 while문을 돌때마다 스택의 전수조사가 된다는걸 간과해버렸다. 때문에 로직은 올바르게 동작하되 극악의 효율을 내버렸다.
결국 알고리즘은 다시 뜯어고쳤다.

우선 NO가 출력되는 경우는 스택인 temp_s의 마지막 값이 다음번 찾을 in_data_list[idx]보다 큰 경우이다. 단순하게 생각해보면
스택은 LIFO인데 입력되는 자연수는 1부터 n까지 오름차순으로 정렬된 형태로 입력된다. 따라서 어느시점에 확인하든 항상
마지막 값이 스택 내에서 가장 큰 값이 된다. 그러니 스택의 마지막 값보다 in_data_list[idx]이 크다는 것은 스택 안에
in_data_list[idx]값이 이미 push 되었단 뜻이다. 그러니 입력된 수열을 만들 수 없게 된다.

위의 사실만 인지하면 다음 로직은 어렵지 않게 해결할 수 있다.

특이한 부분은 in_data_list.append(-1) 이부분과 temp_s, plus_minus_list = [-1, 1], ['+'] 이부분인데 더미값을 넣어
list index out of range를 막으려고 넣었다.

통과는 했지만 보다 나은 성능을 위해 보강해야할 부분이 많은 문제다.

'''


def stack_sequence(in_data_list, in_data_size):
	num = 2
	temp_s, plus_minus_list = [-1, 1], ['+']

	idx = 0

	while len(plus_minus_list) < in_data_size * 2:
		if in_data_list[idx] == temp_s[-1]:
			temp_s.pop()		
			plus_minus_list.append('-')			
			idx += 1
			if temp_s[-1] > in_data_list[idx]:
				return "NO"
		elif in_data_list[idx] != temp_s[-1] and num <= in_data_size:
			temp_s.append(num)
			num += 1
			plus_minus_list.append('+')

	return plus_minus_list

in_data_size = int(input())
in_data_list = []

for i in range(in_data_size):
    in_data_list.append(int(input()))
in_data_list.append(-1)
result = stack_sequence(in_data_list, in_data_size)

if isinstance(result, list):
    for i in result:
        print(i)
else:
    print(result)	
