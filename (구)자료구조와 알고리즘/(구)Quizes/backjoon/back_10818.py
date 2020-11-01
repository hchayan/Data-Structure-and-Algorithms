import sys
x = int(sys.stdin.readline().rstrip())

lis = sys.stdin.readline().rstrip().split()
maxx = int(lis[0])
minn = int(lis[0])
for i in range(x):
  if int(lis[i]) > maxx:
    maxx = lis[i]

  if lis[i] < minn:
    minn = lis[i]
print(minn, maxx)
