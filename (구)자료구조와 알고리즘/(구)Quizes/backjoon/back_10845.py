import sys
num = int(sys.stdin.readline().rstrip())
queue = []
for i in range(int(num)):
	temp = sys.stdin.readline().rstrip().split()
	
	if temp[0] == "push":
		queue.append(temp[1])
	
	elif temp[0] == "pop":
		if len(queue) != 0:
			print(queue[0])
			queue.remove(queue[0])
		else: print(-1)
	
	elif temp[0] == "size":
		print(len(queue))
	
	elif temp[0] == "empty":
		if len(queue) == 0: print(1)
		else: print(0)
	
	elif temp[0] == "front":
		if len(queue) != 0: print(queue[0])
		else: print(-1)
	
	elif temp[0] == "back":
		if len(queue) != 0: print(queue[len(queue)-1])
		else: print(-1)
