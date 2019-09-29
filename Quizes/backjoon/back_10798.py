import sys

temp=[]
max_len=0

for i in range(5):
	x = sys.stdin.readline().rstrip()
	temp.append(x)
	
	if len(x) > max_len:
		max_len = len(x)
		
for i in range(5):
	while len(temp[i]) < max_len:
		temp[i]+=" "

str=""		
for i in range(max_len):
	for j in range(5):
		if temp[j][i] != " ":
			str+=temp[j][i]
		
print(str)
	

	
