import sys
alphabet = [-1] * 26

x = sys.stdin.readline().rstrip()

for i in range(len(x)):
	if alphabet[ord(x[i])-97] == -1:
		alphabet[ord(x[i])-97] = i
		
print(' '.join(map(str,alphabet)))