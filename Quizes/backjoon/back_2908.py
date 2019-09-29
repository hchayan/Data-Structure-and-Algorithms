import sys


tel = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']

x = sys.stdin.readline().rstrip()
ans = 0
for i in x:
	for k in range(len(tel)):
		if i in tel[k]:
			ans = ans + k + 3
			
print(ans)
		


	


	
	
	
	