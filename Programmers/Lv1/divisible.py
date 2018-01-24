'''
[ 나누어 떨어지는 숫자 배열 ]
divisible 메소드는 int형 배열 array와 int divisor를 매개변수로 받습니다.
array의 각 element 중 divisor로 나누어 떨어지는 값만 포함하는 새로운 배열을 만들어서 반환하도록 divisible에 코드를 작성해 보세요.

예를들어 array가 {5, 9, 7, 10}이고 divisor가 5이면 {5, 10}을 리턴해야 합니다.
'''

'''
[ 접근방법 ]
입력받은 list_value를 하나씩 for문으로 가져와 divisor로 나눠보고 0이 나오면 별도의 변수에 담아서 출력하면 된다.

아래 코드는 filter와 lambda를 사용하여 같은 과정을 최소화했다.

'''

def divisible(list_value, divisor):
	return list(filter(lambda x: x%divisor == 0, list_value))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
arr = [5, 9, 7, 10]
print(divisible(arr, 5))