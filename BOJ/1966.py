'''
[ 프린터 큐 ]
여러분도 알다시피 여러분의 프린터 기기는 여러분이 인쇄하고자 하는 문서를 인쇄 명령을 받은 ‘순서대로’, 즉 먼저 요청된 것을 먼저 인쇄한다. 
여러 개의 문서가 쌓인다면 Queue 자료구조에 쌓여서 FIFO - First In First Out - 에 따라 인쇄가 되게 된다. 하지만 상근이는 
새로운 프린터기 내부 소프트웨어를 개발하였는데, 이 프린터기는 다음과 같은 조건에 따라 인쇄를 하게 된다.

    1. 현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
    2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 
    그렇지 않다면 바로 인쇄를 한다.

현재 Queue의 가장 앞에 있는 문서의 ‘중요도’를 확인한다.
나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 하나라도 있다면, 이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치 한다. 그렇지 않다면 바로 인쇄를 한다.
예를 들어 Queue에 4개의 문서(A B C D)가 있고, 중요도가 2 1 4 3 라면 C를 인쇄하고, 다음으로 D를 인쇄하고 A, B를 인쇄하게 된다.

여러분이 할 일은, 현재 Queue에 있는 문서의 수와 중요도가 주어졌을 때, 어떤 한 문서가 몇 번째로 인쇄되는지 알아내는 것이다. 
예를 들어 위의 예에서 C문서는 1번째로, A문서는 3번째로 인쇄되게 된다.

입력 예제)
3               -> test_case
1 0             -> N1, M1
5               -> N1개 문서의 중요도
4 2             -> N2, M2
1 2 3 4         -> N2개 문서의 중요도
6 0
1 1 9 1 1 1

출력 예제)
1
2
5

'''

'''
[ 접근방법 ]
큐 안에 가장 큰 값을 출력하는 것이 핵심이다. 이에따라 큐 내에서 계속 위치가 바뀌는게 우리가 출력하려는 문서가 누구인지를 놓치지 않는것이 중요하다.
마치 돈 넣고 돈 먹는 종이컵 속 동전을 유심히 보는 것과 같다. 
그래서 두개의 큐를 활용했다. 하나는 문서간의 구분을 위해, 하나는 중요도를 반복하기 위해서다.
target은 처음 문서를 A라고 했을때, m번째 문서의 고유 인덱스를 위해 정했다. 큐에서 이 문서가 빠저나가는지 구분하기 위한 id값이다.

'''

def printer_queue(n, m, p_list):
    p_name = [chr(i) for i in range(65, 65+n)]
    target = p_name[m]
    while len(p_list) > 0:
        if p_list[0] == max(p_list):
            p_list.pop(0)
            if p_name.pop(0) == target:
                return n - len(p_list)
        else:
            p_list.append(p_list.pop(0))
            p_name.append(p_name.pop(0))

test_case = int(input())

for t in range(test_case):
    n, m = map(int, input().split())
    priority_list = list(map(int, input().split()))
    print(printer_queue(n, m, priority_list)) 

# https://github.com/bbubbush/algorithm/blob/master/BOJ/1966.py