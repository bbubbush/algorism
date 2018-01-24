'''
[ 행렬의 덧셈 ]
행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 
2개의 행렬을 입력받는 sum_matrix 함수를 완성하여 행렬 덧셈의 결과를 반환해 주세요.

예를 들어 2x2 행렬인 A = ((1, 2), (2, 3)), B = ((3, 4), (5, 6)) 가 주어지면, 
같은 2x2 행렬인 ((4, 6), (7, 9))를 반환하면 됩니다.(어떠한 행렬에도 대응하는 함수를 완성해주세요.)

'''

'''
[ 접근방법 ]
풀이 1번의 경우 우리가 일반적으로 배운 행렬의 덧셈법칙을 적용한 것이다.
물이 2번의 경우 최근에 tensorflow를 공부하면서 numpy를 접한적이 있는데 이를 통해 행렬의 연산을 쉽게 할 수 있다.
(tolist를 붙이지 않으면 ndarray or scalar 형태로 리턴이 된다)

'''

# 풀이 1 - 일반적인 2차원 배열
def sum_matrix(list_a,list_b):
    answer = []
    for i in range(0, len(list_a)):
        temp = []
        for j in range(0, len(list_a[i])):
            temp.append(list_a[i][j] + list_b[i][j])
        answer.append(temp)
    return answer

'''
# 풀이 2 - numpy 사용
import numpy as np

def sum_matrix(list_a, list_b):	
	return np.add(list_a, list_b).tolist()
'''

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(sum_matrix([[1,2], [2,3]], [[3,4],[5,6]]))