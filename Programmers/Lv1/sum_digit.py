'''
[ 자릿수 더하 ]
sum_digit함수는 자연수를 전달 받아서 숫자의 각 자릿수의 합을 구해서 return합니다.
예를들어 number = 123이면 1 + 2 + 3 = 6을 return하면 됩니다.
sum_digit함수를 완성해보세요.

'''

'''
[ 접근방법 ]
알고리즘 문제를 접하다보면 은근히 쉽게 접하는 문제.
나머지를 이용해서 1의 자리를 구하고, 나눠서 자리수를 조절하는 방법으로
쉽게 해결. 프로그래머스의 풀의 강의도 있으니 잘 모르겠으면 참고하면 된다.

'''

def sum_digit(number):
    result = 0
    while number//10 > 0:
        result += number%10
        number = number // 10
    
    return result + number
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : {}".format(sum_digit(123)));
