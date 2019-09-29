import sys

n = int(sys.stdin.readline().rstrip())

lis = []
# 함수 생성
def push(x):
	lis.append(x)
	
def pop():
	print(lis.pop()) if len(lis) != 0 else print(-1)

def size():
	print(len(lis))

def empty():
	print(1) if len(lis) == 0 else print(0)
	
def top():
	print(-1) if len(lis)==0 else print(lis[len(lis)-1])
	

# 실행문
for i in range(n):
	x = sys.stdin.readline().rstrip().split()
	if x[0] == 'push':
		push(int(x[1]))
	elif x[0] == 'pop':
		pop()
	elif x[0] == 'size':
		size()
	elif x[0] == 'empty':
		empty()
	elif x[0] == 'top':
		top()
		

	
	