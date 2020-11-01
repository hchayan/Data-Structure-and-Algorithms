import sys
import math

x = sys.stdin.readline().rstrip().split()

def back_1712(a,b,c):
	if b >= c:
		return -1
		
	if a /(c-b) == a //(c-b):
		return a//(c-b)+1
	
	return math.ceil(a /(c-b))
		

print(back_1712(int(x[0]), int(x[1]), int(x[2])))