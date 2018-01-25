'''
[ 삼각형 출력하기 ]
print_triangle 메소드는 양의 정수 num을 매개변수로 입력받습니다.
다음을 참고해 *(별)로 높이가 num인 삼각형을 문자열로 리턴하는 print_triangle 메소드를 완성하세요
print_triangle return하는 String은 개행문자('\n')로 끝나야 합니다.

높이가 3일때

*
**
***
높이가 5일때

*
**
***
****
*****
'''

'''
[ 접근방법 ]
간단한 별찍기 문제이다.

반복문을 통해 num까지 순차 진행하면서 i에 값에 해당하는 별을 찍고 개행을 해주면 된다.

다만 return 되는 String값은 마지막에 '\n'이 붙어야 한다는 것만 조심해야 한다.

'''

def print_triangle(num):
    return '\n'.join(['*' * (i+1) for i in range(num)]) + '\n'


# 아래는 테스트로 출력해 보기 위한 코드입니다.
print( print_triangle(3) )