'''
[ 평균구하기 ]
함수를 완성해서 매개변수 array의 평균값을 return하도록 만들어 보세요.
어떠한 크기의 array가 와도 평균값을 구할 수 있어야 합니다.
'''

'''
[ 접근방법 ]
말그대로 평균을 구한다. 총합을 전체 갯수로 나눠서 구했다.

'''

def average(list):
    if len(list) == 0: return 0
    return sum(list) / len(list)

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4] 
print("평균값 : {}".format(average(list)))