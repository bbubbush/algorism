'''
[ 소수 구하기 ]
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오. (1 ≤ M ≤ N ≤ 1,000,000)

입력 예제)
3 16

출력 예제)
3
5
7
11
13

'''
        
'''
[ 접근방법 ]
항상 소수나 약수 문제는 시간과의 싸움이다. 문제를 이해 못하는 사람은 없으니 속도전이 될 수 밖에 없다.
약수문제에서 기억해야 할 점은 n의 약수를 구할때는 sqrt(n)까지만 구하면 된다는 점이다.  이 부분만 기억해도 속도가 확연히 오르게 된다.
이유는 sqrt(n) 이전에 나온 약수는 이후에 나오는 다른 약수와 대칭이 되기 때문이다. 

소수 문제를 풀 때는 소수의 특징을 기억해야 한다.

    1) 2외의 모든 소수는 다 홀수이다.
    2) 1은 소수가 아니다.
    3) n보다 작은 소수로 나누어 떨어질 경우 소수가 아니다.(n보다 작은 소수로 나눠보면 소수의 여부를 판단할 수 있다.)
    
아래는 에라토스의 체를 코드로 직접 구현해봤다. 누군가는 빠른 알고리즘이라고 했는데 내가 구현을 잘못했는지 실제로 성능이 좋은편은 아니었다.

결국 전체 배열을 만들어서 revome든 del이든 함수를 자주 호출할수록 성능은 저하되는데 (혹은 0으로 치환해 전체 길이의 영향을 안주든) 이는 이것대로 
속도저하를 유발한다. 

파이썬의 for ~ else문을 다른 언어에서 사용할 수 없으니 boolean값을 두어 체크하는 것이 좋겠다.

'''
import math
import time

def find_prime_number(m, n):
    prime_list = []
    for i in range(m, n+1):
        if i == 2:
            prime_list.append(str(i))

        if i % 2 == 0 or i == 1:
            continue

        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                break
        else:
            prime_list.append(str(i))    
    return "\n".join(prime_list)

#m, n = map(int, input().split())
#print(find_prime_number(m, n))



def eratos(m, n):
    candidates = [i for i in range(m,n+1)]

    if candidates[0] == 1:
        candidates.remove(1)
    for i in candidates:
        if i == 0:
            continue
        for j in range(len(candidates)):
            if candidates[j] == 0 or candidates[j] == i:
                continue
            if candidates[j] % i == 0:
                candidates[j] = 0

    for candidate in candidates:
        if candidate != 0:
            print(candidate)

    

#m, n = map(int, input().split())
#print(find_prime_number(m, n))
s_time = time.time()
print(find_prime_number(1, 10000))
print(time.time()-s_time)
s_time = time.time()
print(eratos(1, 10000))
print(time.time()-s_time)

   