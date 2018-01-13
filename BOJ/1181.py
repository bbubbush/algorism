'''
[ 단어 정렬 ]
알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

길이가 짧은 것부터
길이가 같으면 사전 순으로 출력한다.

단, 중복된 단어는 한번만 출력한다.

            
입력 예제)
13            -> TestCase
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

출력 예제)
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate

'''
        
'''
[ 접근방법 ]
초기 접근방법 : list에 모두 담아 길이별로 정렬하고, 같은 길이 내에서 정렬하려고 함
하지만 시간도 오래 걸리고 코드도 한눈에 들어오지 않아서 사전을 이용하기로 했다.

1) 사전에 word의 길이에 따라 값을 list형태로 담는다.
2) 사전을 key를 기준으로 sort
3) key값을 하나씩 가져오면서 list형태의 value를 set에 담아 중복을 제거
4) 중복을 제거 한 후 sort
5) 하나씩 출력

순으로 코드를 만들었다. 생각보다 쉽게 풀려 재밌었다.


'''

words = {}
for i in range(int(input())):
    word = input()

    # 사전에 word의 길이를 key로 하여 list값으로 입력값을 저장
    if len(word) in words:
        words[len(word)].append(word)
    else:
        words[len(word)] = [word]

# 사전을 key를 기준으로 오름차순
keys = sorted(words)

for key in keys:
    # 중복을 제거하기 위해 리스트를 set에 담은 후 오름차순 정렬
    for word in sorted(set(words[key])):
        print(word)

    

