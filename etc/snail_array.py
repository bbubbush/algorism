'''
[ 달팽이 배열 ]
요소가 int 형이고 행과 열의 길이가 모두 5인 2차원 배열을 선언하고 모든 요소를 0으로 초기화 한후,
'시계방향 달팽이' 형식으로 채워서 출력하는 프로그램을 작성하세요. 단, 반복문을 4개이상 사용할 수는 없습니다.
                
입력 예제)
5, 5    -> m, n


출력 예제)
1	2	3	4	5
16	17	18	19	6
15	24	25	10	7
14	23	22	21	8
13	12	11	10	9

'''
        
'''
[ 접근방법 ]
다양한 방법이 있겠지만 입력된 m, n값에 따라 배열의 테두리를 반복적으로 채워가는 형태로 풀었다.예를 들어 5, 5의 입력의 경우

1	2	3	4	5			1	2	3	4	5
16	0	0	0	6			16	17	18	19	6
15	0	0	0	7	------>		15	24	0	20	7
14	0	0	0	8			14	23	22	21	8
13	12	11	10	9			13	12	11	10	9

위와 같이 첫 사이클에 가장 외각을, 다음 사이클에는 그다음 외각을 채워나가는 형식으로 구했다.

나름의 규칙을 찾았는데 외각의 개수는 2*(m+n)-4였고, 시도해본 TC중 유일한 예외는 m = 1, n = 1인 경우 뿐이었다. 그래서 이 부분을 삼항식으로 분기했다.

처음 j의 값을 초기화할때 (0,0)에 값을 할당하기 위해 -1로 임의로 조정했다. 하나의 사이클이 끝나면 m과 n의 크기를 조절하고 cycle 변수를 증가시킨다.

(issue사항)
배열의 입력이 1*X 형태로 입력이 되면 이상한 값이 입력이 된다. 1*X형태는 달팽이 배열이라고 할수는 없지만 어쨋든 문제가 될 소지가 다분하므로
추후 코드의 수정이 필요하다.
'''

def snail_array(m, n):
    snail_arr = [[0 for j in range(n)] for i in range(m)]
    size = m * n    # 종료조건
    cycle = 0       # 반복횟수면서 동시에 시작점 지정
    last_value = 0  # 마지막 value값을 기록
    while last_value < size:
        i, j = cycle, cycle-1
        end = m*n == 1 and 1 or 2*(m+n)-4   # m과 n이 1일때만 이 규칙이 성립하지 않아서 삼항으로 조건을 줌
        for cnt in range(end):
            if cnt < n:
                j += 1
            elif cnt < n+m-1:
                i += 1
            elif cnt < 2*n+m-2:
                j -= 1
            elif cnt < 2*(n+m)-2:
                i -= 1

            last_value += 1
            snail_arr[i][j] = last_value
            
        m, n = m-2, n-2         # m * n의 크기를 (m-2) * (n-2)크기로 조절
        cycle += 1      # 반복횟수 증가

    # 값 확인하려면 아래주석 풀면 됨
    '''
    for a in snail_arr:
        for b in a:
            print(b, '\t', end='')
        print()
    print()
    '''
    return snail_arr
#print(snail_array(5, 5))
#print(snail_array(3, 3))
#print(snail_array(1, 1))
#print(snail_array(3, 5))
#print(snail_array(10, 9))
print(snail_array(1, 5))    # error TC
    
