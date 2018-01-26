'''
[ 정수 내림차순으로 배치하기 ]
reverse_int 메소드는 int형 n을 매개변수로 입력받습니다.
n에 나타나는 숫자를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
예를들어 n이 118372면 873211을 리턴하면 됩니다.
n은 양의 정수입니다.

'''

'''
[ 접근방법 ]
문제의 지문은 매우 간단하지만 한번에 하려고 하면 어디부터 해야할지 복잡할 수 있는 문제다.

아래와 같은 절차로 접근하면 어렵지 않게 할 수 있다.

1) 입력받은 integer type을 string type으로 형변환한다.
2) 이를 정렬하기 위해 list type으로 형변환 한다.
3) sorted를 사용해서 내림차순으로 정렬한다.
4) 정렬된 list를 join()을 통해 하나의 문자열로 합친다.
5) 마지막으로 integer type으로 형변환한다.

데이터 가공을 위해 형변환을 필요에 따라 해줘 문제를 해결했다.
'''

def reverse_int(n):
	return int(''.join(sorted(list(str(n)), reverse=True)))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(reverse_int(118372))
print(type(reverse_int(118372)))