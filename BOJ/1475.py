'''
[ 방 번호 ]
다솜이는 은진이의 옆집에 새로 이사왔다. 다솜이는 자기 방 번호를 예쁜 플라스틱 숫자로 문에 붙이려고 한다.

다솜이의 옆집에서는 플라스틱 숫자를 한 세트로 판다. 한 세트에는 0번부터 9번까지 숫자가 하나씩 들어있다. 
다솜이의 방 번호가 주어졌을 때, 필요한 세트의 개수의 최소값을 출력하시오. 
(6은 9를 뒤집어서 이용할 수 있고, 9는 6을 뒤집어서 이용할 수 있다.)

입력 예제)
9999

출력 예제)
2

'''

'''
[ 접근방법 ]
입력된 숫자를 문자열로 생각하여 하나씩 본인의 갯수를 증가시키면 된다. 다만 6과 9는 두 숫자지만 뒤집어서
서로를 대체 가능하므로 하나의 값으로 생각한다.
숫자 리스트(혹은 딕셔너리) 중에서 최대값을 출력하면 답을 구할 수 있다. 아래 코드는 딕셔너리로 구현했지만
리스트를 사용하면 max함수를 사용할 수 있어 두번째 for문을 안써도 답을 구할 수 있다.
	
'''

inData = int(input())

chkNumber = {str(i) : 0 for i in range(10)}
maxVal = 0
sixAndNine = 0
for i in str(inData):
    chkNumber[i] += 1


for key in chkNumber:
    if key == '9' or key == '6':
        sixAndNine += chkNumber[key]
        continue
    maxVal = max(maxVal, chkNumber[key])

sixAndNine = sixAndNine // 2 + sixAndNine % 2 
print(max(maxVal, sixAndNine))
    
