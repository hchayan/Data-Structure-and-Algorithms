import sys
n, x = map(int, sys.stdin.readline().rstrip().split())
print(sorted(list(map(int,sys.stdin.readline().rstrip().split())))[x-1])