# 파스칼의 삼각형
import sys

n, k = list(map(int,sys.stdin.readline().rstrip().split()))

def pascal(x,y):
    if x == 0 or y ==0 or x==y:
        return 1
    return pascal(x-1,y-1)+pascal(x-1,y)

print(pascal(n,k))


'''
def factorial(x):
    if x == 1:
        return 1
    return x*factorial(x-1)

if k<0 or k > n:
    print(0)
else:
    print(factorial(n)//(factorial(k)*factorial(n-k)))
'''

