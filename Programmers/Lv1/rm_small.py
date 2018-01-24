'''
[ 제일 작은 수 제거하기 ]
rm_small함수는 list타입 변수 mylist을 매개변수로 입력받습니다.
mylist 에서 가장 작은 수를 제거한 리스트를 리턴하고, mylist의 원소가 1개 이하인 경우는 []를 리턴하는 함수를 완성하세요.
예를들어 mylist가 [4,3,2,1]인 경우는 [4,3,2]를 리턴 하고, [10, 8, 22]면 [10, 22]를 리턴 합니다.
'''

'''
[ 접근방법 ]
sorting 후에 myList[1:] 식으로 출력하려 했으나 이러면 원형이 달라진다.

그래서 그냥 min값 찾아 삭제한 myList를 출력했다.

'''

def rm_small(myList):
    myList.remove(min(myList))
    return myList

# 아래는 테스트로 출력해 보기 위한 코드입니다.
my_list = [4, 3, 2, 1]
print("결과 {} ".format(rm_small(my_list)))
my_list = [1]
print("결과 {} ".format(rm_small(my_list)))