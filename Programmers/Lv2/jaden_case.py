'''
[ JadenCase 문자열 만들기 ]
jaden_case함수는 문자열 s을 매개변수로 입력받습니다.
s에 모든 단어의 첫 알파벳이 대문자이고, 그 외의 알파벳은 소문자인 문자열을 리턴하도록 함수를 완성하세요
예를들어 s가 3people unFollowed me for the last week라면 3people Unfollowed Me For The Last Week를 리턴하면 됩니다.

'''

'''
[ 접근방법 ]
모든 문자의 시작을 대문자로, 나머지는 소문자로 변경하는 문제이다.

처음에는 ' '을 기준으로 split을 했는데 공백이 연속되는 문자열을 입력받을 경우 문제가 발생한다. 그래서 원초적인 방법으로 풀었다.

1) 모든 문자열을 소문자로 바꾼다.
2) cnt라는 변수를 통해 현재 단어의 어디를 변환중인지 위치값을 저장한다.
3) 공백(' ')을 만나면 cnt를 초기화 시킨다.
4) 이 외에는 cnt가 1인 경우에는 대문자를, 그 외에는 문자 그대로를 더했다.(1의 과정에서 모든 문자열을 이미 소문자로 치환했다.)

위의 과정을 염두하면서 코드를 짯다. 
4의 과정중 cnt가 1인 경우라는 조건에 더해 공백이 아닌 것도 추가했는데 이것이 없으면 공백이 연속해서 발생할 경우 연속된 단어로 인식해서
연속된 공백 이후에 나오는 단어의 첫 알파벳이 소문자로 나오게 된다.

다른 사람의 풀이를 보다가 문자열의 내장함수인 title이 같은 기능을 제공한다는 것을 알게 되었다.

'''

def jaden_case(s):
    s = s.lower()
    cnt, result = 0, ''
    for word in s:
        cnt += 1
        if cnt == 1 and word != ' ':    # cnt가 1인 경우면서 공백이 아닌 경우 
            result += word.upper()
        elif word == ' ':               # 공백을 만나면 cnt 초기화
            result += ' '
            cnt = 0
        else:
            result += word
    return result

    # 내장함수를 사용하여 푼 경우
    #return s.title()
     
# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(jaden_case("3people unFollowed me for the last week"))
print(jaden_case("   3people     unFollowed me    for  the    last    week"))