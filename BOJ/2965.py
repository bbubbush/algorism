def kangaroo(a, b, c, cnt):
    if a + 1 == b and c - 1 == b:
        return cnt
    if a < b and b < c:
        return max(kangaroo(b, b+1, c, cnt + 1), kangaroo(a, b-1, b, cnt + 1))
    return cnt - 1    
    
    
    
a, b, c = map(int, input().split())
if a < b and b < c:
    print(kangaroo(a, b, c, 0))
else:
    print(0)

    
