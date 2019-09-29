import sys

x = sys.stdin.readline().rstrip().split()

for i in range(1,int(x[0])+1):
    if i*int(x[1])%int(x[0]) == 0:
        maxx = i*int(x[1])
        print(maxx//((maxx//int(x[1]))*((i*int(x[1]))//int(x[0]))))
        print(maxx)
        break