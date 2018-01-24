'''
[ 최대값과 최소값 ]
get_min_max_string 메소드는 String형 변수 str을 매개변수로 입력받습니다.
str에는 공백으로 구분된 숫자들이 저장되어 있습니다.
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 (최소값) (최대값)형태의 String을 반환하는 메소드를 완성하세요.
예를들어 str이 1 2 3 4라면 1 4를 리턴하고, -1 -2 -3 -4라면 -4 -1을 리턴하면 됩니다.
'''

'''
[ 접근방법 ]
크게 두가지 방법을 생각했다.

1) 오름차순 정렬을 한 후, 0번째 값과 -1번째 값을 출력한다
2) min, max 함수를 이용해서 정렬없이 바로 한다.

개인적으로는 1번이 좋은 것 같다. min이나 max의 경우 결국 s의 길이를 n이라고 할때 각각이 n번만큼의 순회를 한다.

하지만 정렬은 n번만 수행하면 된다.
(sort()함수의 경우 Tim sort를 사용하며 Merge sort의 변형이다. Merge sort의 평균 시간복잡도는 O(nlogn))

가장 빠른 sorting algorithm이다. (quick sort도 O(nlogn)의 시간복잡도를 갖지만 worst case에서는 O(n^2)이다.)

'''

def get_min_max_string(s):
	s_list = sorted(s.split(' '))
	return "{} {}".format(s_list[0], s_list[-1])		# case1
	#return "{} {}".format(min(s_list), max(s_list))	# case2

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(get_min_max_string("1 2 3 4 -1"))