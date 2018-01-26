'''
[ 행렬의 곱셈 ]
행렬의 곱셈은, 곱하려는 두 행렬의 어떤 행과 열을 기준으로, 좌측의 행렬은 해당되는 행, 우측의 행렬은 해당되는 열을 순서대로 곱한 값을 더한 값이 들어갑니다. 
행렬을 곱하기 위해선 좌측 행렬의 열의 개수와 우측 행렬의 행의 개수가 같아야 합니다. 
곱할 수 있는 두 행렬 A,B가 주어질 때, 행렬을 곱한 값을 출력하는 product_matrix 함수를 완성해 보세요.

'''

'''
[ 접근방법 ]
두 행렬 이 아래와 같이 있을 때, 행렬의 곱은 다음과 같다.

a = [					b = [					a * b = [
		[a11, a12],				[b11, b12],					[a11*b11 + a12*b21, a11*b12 + a12*b22],
		[a21, a22]				[b21, b22]					[a21*b11 + a22*b21, a21*b12 + a22*b22]
	]						]							]

이처럼 계산한다. 

물론 우리는 우수한 정규교육과정을 겪은 인재들이기 때문에 모두 알지만 세월의 힘에 의해 까먹었을뿐이다.

이제는 우리가 알고있는 과정을 코드로 구현하는 일만 남았다. 하지만 이게 쉽지 않다. 변수들도 헷갈리고 test case의 답을 노트에 푼 내 답과 학인하는 것도 큰 일이 된다.

그래서 파이썬은 numpy를 통해 우리의 고충을 덜어준다.
numpy는 행렬에 관한 연산에 적합한 라이브러리다. 그러니 문명의 편리함을 받아들여 복잡한 연산은 컴퓨터에게 맡겨보자!

아 한가지 조심해야 할 점은 행렬의 곱은 A의 행과 B의 열의 길이가 같아야 한다. A가 n * m 의 형태면 B는 m * k 의 형태여야 연산이 가능하다.
참고로 위 상황의 A * B는 n * k 형태의 행렬로 나올 것이다.

'''
import numpy as np
def product_matrix(A, B):
    if len(A[0]) != len(B):
        return -1
    answer = []

    for i in range(len(A)):
        tempList = []
        for j in range(len(B[0])):
            temp = 0
            for k in range(len(A[0])):
                temp += A[i][k] * B[k][j]
            tempList.append(temp)
        answer.append(tempList)
    #return answer
    return np.matmul(A, B).tolist()

# 아래는 테스트로 출력해 보기 위한 코드입니다.
a = [[1, 2, 3], [2, 3, 4], [1, 2, 3]]
b = [[3, 4, 5], [5, 6, 7], [3, 4, 5]]
print("결과 : {}".format(product_matrix(a,b)))
a = [[1, 2, 3]]
b = [[5], [6], [3]]
print("결과 : {}".format(product_matrix(a,b)))