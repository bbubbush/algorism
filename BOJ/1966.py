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
