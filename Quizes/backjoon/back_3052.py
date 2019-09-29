# 주요 개념 : 배열

import sys

lis = []

for i in range(10):
  x = int(sys.stdin.readline().rstrip())
  if x%42 not in lis:
    lis.append(x%42)
    
print(len(lis))