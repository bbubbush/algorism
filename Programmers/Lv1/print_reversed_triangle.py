'''
[ 역삼각형 출력하기 ]
print_reversed_triangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
다음을 참고해 *(별)로 높이가 num인 삼각형을 문자열로 리턴하는 print_reversed_triangle 메소드를 완성하세요

높이(num)가 3일때 다음과 같은 문자열을 리턴하면 됩니다.

***
**
*
'''

'''
[ 접근방법 ]
간단한 별찍기 문제다.
반복문을 써서 num부터 0까지 -1씩 이동하면서 i만큼 별을 찍었다. 순행하면서 하려면

for i in range(num):
	print('*' * (num - i))

이런 식으로 풀면 된다.

'''

def print_reversed_triangle(num):
    return '\n'.join(['*' * i for i in range(num, 0, -1)])

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(print_reversed_triangle(3))