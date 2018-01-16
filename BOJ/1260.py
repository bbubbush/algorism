'''
[ DFS와 BFS ]
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 
정점 번호는 1번부터 N번까지이다.

입력 예제)
4 5 1       -> N, M, V
1 2         -> edge[0]
1 3
1 4
2 4
3 4         -> edge[M-1]

출력 예제)
1 2 4 3     -> DFS
1 2 3 4     -> BFS

'''
'''
[ 접근방법 ]
상상개발자 : https://www.youtube.com/watch?v=BLc3wzvycH8&index=16&list=PLVNY1HnUlO25sSWDr7CzVvkOF3bUgkiQQ
이분의 강의를 참고하여 만들었다.

DFS는 stack을, BFS는 queue를 사용한다는 큰 차이점을 제외하면 큰 틀은 같다. 우선 3가지의 재료가 필요하다.

1) vertex들이 담여있는 list(이하 vertex_list)
2) vertex간 edge를 담아 둔 list(이하 edge_list)
3) vertext 개별이 연결되어있는 다른 vertext를 담아 둔 list(이하 adjacency_list)

1)번과 2)번을 통해 3)을 만들어 낼 수 있다.

다음으로 DFS는 stack에, BFS는 queue에 시작하는 vertex값인 v를 넣어주어 강의 속 방법을 그대로 따라했다.
다만, 문제 설명에 조건으로 '방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문한다'항목 때문에
DFS는 len(adjacency_list[current-1])가 2 이상이면 내림차순을, BFS는 오름차순을 해주면 된다.
또한 강의속 예제를 따라할땐 괜찮았는데 BOJ예제를 입력할 땐 특정값이 중복되어 visitedList에 담겨서 
이미 담긴 값은 if문을 통해 뺐다.

'''


n, m, v = map(int, input().split())
vertex_list = [i for i in range(1, n+1)]

edge_list = []

for i in range(m):
    start, end = map(int, input().split())
    edge_list.append((start, end))
    edge_list.append((end, start))

adjacency_list = [[] for vertex in vertex_list]

for edge in edge_list:
    adjacency_list[edge[0]-1].append(edge[1])

# DFS
stack = [v]
visitedList = []

while stack:

    current = stack.pop()
    if len(adjacency_list[current-1]) > 1:  # sort
        adjacency_list[current-1].sort(reverse=True)
    for neighbor in adjacency_list[current-1]:            
        if not neighbor in visitedList:            
            stack.append(neighbor)
    if not current in visitedList:
        visitedList.append(current)

# print DFS
[print(i, end = ' ') for i in visitedList]
print()

# BFS
queue = [v]
visitedList = []
while queue:
    current = queue.pop(0)
    if len(adjacency_list[current-1]) > 1:  # sort
        adjacency_list[current-1].sort()
    for neighbor in adjacency_list[current-1]:
        if not neighbor in visitedList:
            queue.append(neighbor)
    if not current in visitedList:
        visitedList.append(current)

# print BFS
[print(i, end = ' ') for i in visitedList]

# https://github.com/bbubbush/algorithm/blob/master/BOJ/1260.py