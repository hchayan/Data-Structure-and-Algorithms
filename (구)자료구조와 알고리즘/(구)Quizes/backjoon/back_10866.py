import sys

n = int(sys.stdin.readline().rstrip())

tmp = []
for i in range(n):
	x = sys.stdin.readline().rstrip().split()
	
	if x[0] == "push_front":
		tmp = [x[1]]+tmp
		
	elif x[0] == "push_back":
		tmp = tmp+ [x[1]]
	
	elif x[0] == "pop_front":
		if len(tmp) != 0:
			print(tmp[0])
		else:
			print(-1)
		tmp = tmp[1:]
		
	elif x[0] == "pop_back":
		if len(tmp) != 0:
			print(tmp.pop())
		else:
			print(-1)
		
	elif x[0]=="size":
		print(len(tmp))
		
	elif x[0] == "empty":
		if len(tmp) == 0:
			print(1)
		else:
			print(0)
	
	elif x[0] == "front":
		if len(tmp)==0:
			print(-1)
		else:
			print(tmp[0])
	
	elif x[0] == "back":
		if len(tmp)==0:
			print(-1)
		else:
			print(tmp[len(tmp)-1])

		