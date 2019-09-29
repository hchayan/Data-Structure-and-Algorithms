import sys

x = sys.stdin.readline().rstrip().upper()


alpha = []
for i in x:
	if i not in alpha:
		alpha.append(i)
		alpha.append(1)
	else:
		alpha[alpha.index(i)+1]+=1
		
pos = 0	
maxx = 0
semi_max = 0
for k in range(1,len(alpha),2):
	if alpha[k] >= maxx:
		semi_max = maxx
		maxx = alpha[k]
		pos = k 
		
if maxx== semi_max:
	print("?")
else:
	print(alpha[pos-1])