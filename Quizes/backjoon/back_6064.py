import sys

def maxim(a,b):
    m = a%b
    while m > 0:
        a = b
        b= m
        m = a%b
    return b

n = int(sys.stdin.readline().rstrip())

for nn in range(n):
    x = list(map(int,sys.stdin.readline().rstrip().split()))
    flag = False
    for i in range(x[2], x[0]*x[1]//maxim(x[0],x[1])+1, x[0]):
        if i%x[1] == x[3]%x[1]:
            print(i)
            flag = True
            break

    if flag==False:
        print(-1)

'''
통과는 했으나 시간은 많이 걸림
풀이 원리는 우선 문저에서 M과 x를 보고 나올수 있는 값을 N과 y에 대입해보며 둘다 만족하는 값이 있으면 출력.
그리고 범위는 두수 M과 N의 최소공배수이므로, 최소공배수를 구하는 함수를 작성

ex) 10 12 3 9
10, 3만 봤을때 정답이 될수 있는 값 => 3, 13, 23, 33...
이 3, 13, 23, 33의 값을 12와 9에 성립하는 값이 있는지 확인 => 33 (33%12 = 9).
최대값은 10와 12의 최소공배수인 60까지(즉, 마지막은 60번째 해)
'''
