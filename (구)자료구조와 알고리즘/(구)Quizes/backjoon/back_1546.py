# 주요 개념 : 배열
import sys

x = int(sys.stdin.readline().rstrip())

lis = sys.stdin.readline().rstrip().split(" ")

maxx = 0
total = 0
for i in range(x):
  if int(lis[i]) > maxx:
    maxx = int(lis[i])
  total += int(lis[i])

print((total/x)/maxx*100)