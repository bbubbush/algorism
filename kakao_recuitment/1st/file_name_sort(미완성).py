'''
[ 파일명 정렬 ]

입력 예제)
lzw("KAKAO")
lzw("TOBEORNOTTOBEORTOBEORNOT")
lzw("ABABABABABABABAB")

출력 예제)  
[11, 1, 27, 15]
[20, 15, 2, 5, 15, 18, 14, 15, 20, 27, 29, 31, 36, 30, 32, 34]
[1, 2, 27, 29, 28, 31, 30]

'''

'''
[ 접근방법 ]

'''
import re


def file_name_sort(in_data):
    p = re.compile('[0-9]+')
    result = []
    in_data.sort()
    print(in_data)
    for data in in_data:
        number = p.search(data).group()
        head = data.split(number)
        head, tail = data.split(number)[0], data.split(number)[1]
        result.append([head, number, tail])

    result.sort()
    
    return result
    
data = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
print(file_name_sort(data))

# http://tech.kakao.com/2017/11/14/kakao-blind-recruitment-round-3/
