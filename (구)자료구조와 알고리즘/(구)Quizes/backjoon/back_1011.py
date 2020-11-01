import sys
import math
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x = sys.stdin.readline().rstrip().split()
    leng = int(x[1])- int(x[0])
    ans = 0
    while leng > 0:
        max_val = int(math.sqrt(leng))
        leng -= max_val
        ans += 1
    print(ans)

'''
4 = 1 2 1
9 = 1 2 3 2 1
16 = 1 2 3 4 3 2 1
와 같은 결과에서
요소의 최대값이 수의 합의 제곱근.floor이라는 결과를 발견.
이를 이용해, 
가장 큰수부터 제거해나가면서 수의 제곱근.floor를 하나씩 빼면 결과를 구할수 있다.
(math 내장함수를 사용했기에 느리므로, 빠른 실행 속도를 원하면 for문을 이용해 max_Val값을 구하면 된다)
'''
