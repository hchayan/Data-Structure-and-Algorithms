import sys

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    x = sys.stdin.readline().rstrip().split()  # a,b,c = sys.stdin... 식으로 작성후 사용해도 된다..
    a = int(x[2])%int(x[0])  # a : 층수
    b = int(x[2])/int(x[0])  # b : 호수

    if a == 0:
        a = int(x[0])

    if b != int(b):
        b +=1

    print(str(a)+'0'+str(int(b))) if b < 10 else print(str(a)+str(int(b)))
