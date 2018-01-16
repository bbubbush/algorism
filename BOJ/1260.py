

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
    if len(adjacency_list[current-1]) > 1:
        adjacency_list[current-1].sort(reverse=True)
    for neighbor in adjacency_list[current-1]:            
        if not neighbor in visitedList:            
            stack.append(neighbor)
    if not current in visitedList:
        visitedList.append(current)

[print(i, end = ' ') for i in visitedList]
print()

# BFS
queue = [v]
visitedList = []
while queue:
    current = queue.pop(0)
    if len(adjacency_list[current-1]) > 1:
        adjacency_list[current-1].sort()
    for neighbor in adjacency_list[current-1]:
        if not neighbor in visitedList:
            queue.append(neighbor)
    if not current in visitedList:
        visitedList.append(current)

[print(i, end = ' ') for i in visitedList]


