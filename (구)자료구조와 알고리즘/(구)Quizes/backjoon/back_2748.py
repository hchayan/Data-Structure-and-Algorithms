import sys


f1, f2 = 0, 1

for i in range(int(sys.stdin.readline().rstrip())):
    f1,f2 = f2, f1+f2

print(f1)

