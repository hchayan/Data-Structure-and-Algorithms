import sys
x = sys.stdin.readline().rstrip().split()
print(min(int(x[2])-int(x[0]), int(x[3])-int(x[1]), int(x[0]), int(x[1])))