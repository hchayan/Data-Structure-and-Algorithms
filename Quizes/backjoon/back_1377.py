import sys

n = int(sys.stdin.readline().rstrip())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline().rstrip()))

change = False
for i in range(1,n+1):
    change = False
    for j in range(n-i):
        print(i,j)
        if (a[j] > a[j+1]):
            change = True
            a[j], a[j+1] = a[j+1], a[j]
    print(a, change)
    if change == False:
        print(i)
        break;
