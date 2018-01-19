'''
[ N진수 게임 ]
튜브가 활동하는 코딩 동아리에서는 전통적으로 해오는 게임이 있다. 이 게임은 여러 사람이 둥글게 앉아서
숫자를 하나씩 차례대로 말하는 게임인데, 규칙은 다음과 같다.

    1. 숫자를 0부터 시작해서 차례대로 말한다. 첫 번째 사람은 0, 두 번째 사람은 1, … 열 번째 사람은 9를 말한다.
    2. 10 이상의 숫자부터는 한 자리씩 끊어서 말한다. 즉 열한 번째 사람은 10의 첫 자리인 1, 열두 번째 사람은 둘째 자리인 0을 말한다.
    
이렇게 게임을 진행할 경우,
0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 0, 1, 1, 1, 2, 1, 3, 1, 4, …
순으로 숫자를 말하면 된다.

한편 코딩 동아리 일원들은 컴퓨터를 다루는 사람답게 이진수로 이 게임을 진행하기도 하는데, 이 경우에는
0, 1, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, …
순으로 숫자를 말하면 된다.

이진수로 진행하는 게임에 익숙해져 질려가던 사람들은 좀 더 난이도를 높이기 위해 이진법에서 십육진법까지 모든 진법으로
게임을 진행해보기로 했다. 숫자 게임이 익숙하지 않은 튜브는 게임에 져서 벌칙을 받는 굴욕을 피하기 위해,
자신이 말해야 하는 숫자를 스마트폰에 미리 출력해주는 프로그램을 만들려고 한다. 튜브의 프로그램을 구현하라.

2 ≦ n ≦ 16
0 ＜ t ≦ 1000
2 ≦ m ≦ 100
1 ≦ p ≦ m


입력 예제)
n_game(2, 4, 2, 1)
n_game(16, 16, 2, 1)
n_game(16, 16, 2, 2)

출력 예제)
"0111"
"02468ACE11111111"
"13579BDF01234567"
'''

'''
[ 접근방법 ]
진법 변환문제이다. 카카오문제는 항상 두번 이상 생각하게 만드는 것 같다.
일단 숫자처럼 보이지만 모든 결과는 문자열로 반환하기 때문에 중간중간 문자열로 변환했다.

진법변환은 while문을 통해 나머지를 활용했다.

가장 고민이 된건 t개의 결과를 출력해야하는데 result에서 t개를 어떻게 가져오느냐 였는데
[result[m*i+p-1] for i in range(t)]를 통해 해결했다.
결국 t만큼의 결과가 필요하니깐 0부터 t까지 반복하고, t에 m과 p값을 활용해 index를 구했다.


참고로 이 문제는 챔퍼나운 수 라는 수학상수를 이용한 문제라고 한다.
이를 활용해서 풀고싶어서 문제를 찾아봤는데 project euler의 40번 문제로 이가 있으나
10진법 내에서의 풀이과정들 뿐이다. 10진법 내에서 만드는 것이라면
보다 깔끔한 코드를 만들 수 있을 것 같다.


'''


def n_game(n, t, m, p):
    result = "0"
    val_list = ['A', 'B', 'C', 'D', 'E', 'F']
    for i in range(t*m):
        number = i
        temp_list = []
        
        while number > 0:
            val = number % n
            if val > 9:
                temp_list.append(val_list[val % 10])
            else:
                temp_list.append(str(val))

            number = number // n
        
        temp_list.reverse()
        result += ''.join(temp_list)
        if len(result) >= m * t: break    
    return ''.join([result[m*i+p-1] for i in range(t)])



# print(n_game(2, 4, 2, 1))
# print(n_game(16, 16, 2, 1))
print(n_game(16, 1000, 100, 1))



# http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/