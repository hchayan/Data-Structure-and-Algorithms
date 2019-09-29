# 주요개념 : 배열, round : 반올림
import sys

x = int(sys.stdin.readline().rstrip())
ans_list=[]
for i in range(x):
	lis = list(map(int, sys.stdin.readline().rstrip().split(" ")))
	
	total = sum(lis[1:])
		
	ans = 0
	for k in range(1, int(lis[0])+1):
		if int(lis[k]) > total/int(lis[0]):
			ans+=1
	
	ans_list.append("%0.3f"%round(ans/lis[0]*100, 3))
	
for i in ans_list:
	print(str(i)+"%")
	
		
		