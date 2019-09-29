import sys
import math

n = int(sys.stdin.readline().rstrip())


def getAns():
	x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().rstrip().split())
	leng = math.sqrt((x2-x1)**2+(y2-y1)**2)

	if r1 == r2 and x1 == x2 and y1 == y2:
		return -1
	if r1 > r2:
		r1, r2 = r2, r1

	if leng > r1+r2:
		return 0
	elif leng == r1+r2:
		return 1
	else:
		if leng+r1 == r2:
			return 1
		elif leng+r1 < r2:
			return 0
		return 2


for nn in range(n):
	print(getAns())




