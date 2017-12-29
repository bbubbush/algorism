def cainCal(m, n, x, y):
    _x, _y = 1, 1
    end = (m * n) % 2 == 0 and m * n // 2 or m * n

    #print('x\t', 'y\t', 'i')
    for i in range(1, end + 1):
        if _x > m:
            _x = 1

        if _y > n:
            _y = 1

        if _x == x and _y == y:
            return i
            
        #print(_x, '\t', _y, '\t', i)
        
        _x += 1
        _y += 1
    else:
        return -1
        print(-1)

for i in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(cainCal(m, n, x, y))



