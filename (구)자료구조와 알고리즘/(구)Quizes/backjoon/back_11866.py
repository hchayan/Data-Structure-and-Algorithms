import sys
import queue

n = sys.stdin.readline().rstrip().split()

q = queue.Queue();

for i in range(int(n[0])):
	q.put(i+1)
	
ans = []
i=1
while q.qsize()!=0:
	if i%int(n[1]) == 0:
		ans.append(q.get())
	else:
		q.put(q.get())
	i+=1
		
print("<"+", ".join(list(map(str,ans)))+">")

