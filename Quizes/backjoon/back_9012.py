#스택

import sys

n = int(sys.stdin.readline().rstrip())
for i in range(n):
	xx = sys.stdin.readline().rstrip()
	temp = []
	for x in xx:
		if x== "(":
			temp.append(x)
		elif x==")":
			if len(temp) !=0 and temp[len(temp)-1]!=")":
				temp.pop()
			else:
				temp.append(x)
			
	print("YES") if len(temp) == 0 else print("NO")
	
	


	
