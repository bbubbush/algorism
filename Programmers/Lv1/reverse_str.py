'''
[ 문자열 내림차순으로 배치하기 ]
reverseStr 메소드는 String형 변수 str을 매개변수로 입력받습니다.
str에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 String을 리턴해주세요.
str는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
예를들어 str이 Zbcdefg면 gfedcbZ을 리턴하면 됩니다.
'''

'''
[ 접근방법 ]
파이썬은 list에 많은 강점이 있다. 문자열은 사실 문자의 배열의 의미이기 때문에
'Zbcdefg' = ['Z','b','c','d','e','f','g']
이렇게 된다.
따라서 이를 아래와 같이 역으로 출력해주면 된다. 

	answer = ''
	for i in range(len(str_value)-1, -1, -1):
		answer += str_value[i]
	return answer

사실 list의 3번째 인자를 이용하면 한줄로 구할 수도 있다 ㅋ
list[arg1:(arg2):(arg3)]
arg1 : list의 시작지점의 index
arg2 : list의 끝나는 지점의 index(5라고 입력하면 4까지 출력한다)
arg3 : arg1에서 arg2로 움직이는 index값을 설정. 기본값은 1이다.

'''

def reverse_str(str_value):
	return str_value[::-1]

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(reverse_str('Zbcdefg'))
print(reverse_str('gfedcbZ'))