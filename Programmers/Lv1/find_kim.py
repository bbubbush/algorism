'''
[ 서울에서 김서방 찾기 ]
findKim 함수(메소드)는 String형 배열 seoul을 매개변수로 받습니다.

seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하세요.
seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

'''

'''
[ 접근방법 ]
전제 조건이 1) seoul에 Kim은 오직 한번, 2) 잘못된 값이 입력된 경우는 없다  이다.
딱 한번 등장하는 Kim을 찾아서 index값을 반환하기만 하면 된다.
그래서 for문으로 돌면서 value가 Kim이면 그때의 index를 반환했다.
'''


def findKim(seoul):
    kimIdx = 0
    for i, body in enumerate(seoul):
        if( body == 'Kim' ): 
        	kimIdx = i 
        	break
        
    return "김서방은 {}에 있다".format(kimIdx)


# 실행을 위한 테스트코드입니다.
print(findKim(["Queen", "Tod", "Kim"]))