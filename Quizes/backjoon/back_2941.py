import sys
croatia = ['c=','c-','dz=','d-','lj','nj','s=','z=']

x = sys.stdin.readline().rstrip()

print(len(x)-sum(map(x.count,croatia)))

'''
for i in croatia:
	while i in x:
		x = x[:x.index(i)]+","+x[x.index(i)+len(i):]
			
print(len(x))
'''


