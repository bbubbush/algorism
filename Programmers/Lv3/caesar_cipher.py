'''
[ 시저 암호 ]
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을
시저 암호라고 합니다. A를 3만큼 밀면 D가 되고 z를 1만큼 밀면 a가 됩니다.
공백은 수정하지 않습니다. 보낼 문자열 s와 얼마나 밀지 알려주는 n을 입력받아
암호문을 만드는 caesar 함수를 완성해 보세요.
“a B z”,4를 입력받았다면 “e F d”를 리턴합니다.
'''

'''
[ 접근방법 ]
처음엔 매개변수 s가 공백으로 값을 구분하기에 for i in s 를 통해 한번에 해결하려 했지만
다수의 if문으로 인한 코드 가독성의 저하로 대문자, 소문자의 각각의 리스트를 만들어 n만큼
순회한 값을 출력
n이 큰 수일 경우 연산이 느려지므로 나머지 값을 이용해 이를 해결

'''


def caesar(s, n):
    result = ""
    upperAlpha = [chr(i) for i in range(65, 91)]
    lowerAlpha = [chr(i) for i in range(97, 123)]

    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            result += upperAlpha[(ord(i)-65+n) % 26]
        if ord(i) >= 97 and ord(i) <= 122:
            result += lowerAlpha[(ord(i)-97+n) % 26]
        if ord(i) is 32:
            result += ' '
                
    return result


# 실행을 위한 테스트코드입니다.
print('s는 "a B z", n은 4인 경우: ' + caesar("a B z", 4))
