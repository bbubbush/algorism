'''
[ 2016년 ]
2016년 1월 1일은 금요일입니다. 2016년 A월 B일은 무슨 요일일까요?
두 수 A,B를 입력받아 A월 B일이 무슨 요일인지 출력하는 get_day_name 함수를 완성하세요.
요일의 이름은 일요일부터 토요일까지 각각
    SUN,MON,TUE,WED,THU,FRI,SAT
를 출력해주면 됩니다.
예를 들어 A=5, B=24가 입력된다면 5월 24일은 화요일이므로 TUE를 반환하면 됩니다.
'''

'''
[ 접근 방법 ]
datetime 클래스의 weekday() 함수를 이용하면 입력된 날짜의 요일을 숫자로 리턴해준다.
그래서 리턴될 값의 리스트를 순서에 맞게 만들어 준 뒤 weekday를 통해 나온 값을 인덱스로
사용했다.  참고로 월요일은 0으로 리턴된다. 문제에 있는 2016년 1월 1일을 넣어보면
금요일의 값이 4로 리턴되는 것을 통해 유추할 수 있다.
'''


import datetime
def get_day_name(a,b):
    list = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

    return list[datetime.date(2016, a, b).weekday()]

#아래 코드는 테스트를 위한 출력 코드입니다.
print(get_day_name(5,24))
