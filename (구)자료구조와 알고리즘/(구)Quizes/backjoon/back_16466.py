
num = int(input())
lis = input().split()

lis.sort()
for i in range(num):
	if int(lis[i]) != i+1:
		break
	else:
		i+=1
print(str(i+1))










"""
처음에 for문 넣고 그 안에 if 문으로 list안에 해당 원소 없으면 출력. 했는데 시간초과 =? o(n^2)

"""