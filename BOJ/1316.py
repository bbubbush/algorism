'''
[ 그룹 단어 체커 ]
그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다.
예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서
나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.
입력 예제)
3
happy
new
year

출력 예제)
3

'''

'''
[ 접근방법 ]
말 그대로 입력받은 단어 중에 그룹단어에 속하는 애들이 몇개인지 확인해주는 프로그램을 만들면 된다.
일단 비교를 위해 단어의 i번째와 i+1번째를 비교해 달라지는 경우에 로직을 돌려주면 되는데 이때 마지막
문자는 비교가 안되기 때문에 임의로 입력값으로 올 수 없는 공백을 맨 뒤에 더하여 마지막 문자가 이전에
입력이 되었는지 체크해준다.

'''

def checkGroupWord(word):
    alpha = {chr(i) : False for i in range(97, 123)}
    word += ' '     # 맨 마지막에 임의로 공백을 더함
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            if alpha[word[i]] == True:  # 이전에 나온 알파벳이기 때문에 False를 리턴
                return False
            else:
                alpha[word[i]] = True   # 처음 등장했으므로 해당 알파벳을 True로 전
    return True


inputCnt = int(input())
inData = [input() for i in range(inputCnt)]

answer = 0

for word in inData:
    answer += checkGroupWord(word) == True and 1 or 0

print(answer)

        
