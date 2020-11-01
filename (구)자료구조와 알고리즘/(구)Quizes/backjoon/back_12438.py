#수학
import sys

n = int(sys.stdin.readline().rstrip())

for r in range(n):
	x = sys.stdin.readline().rstrip().split()
	n = 0
	namugi = 0                                                # 전과정에서 받아온 나머지
	
	for i in range(int(x[0])):

		b = int(x[1])//int(x[2])                              # b = 몫, c = 나머지
		c = int(x[1])%int(x[2])
		
		if namugi != 0:                                       # 전에 실행한 결과의 나머지값이 있을때,
			c = c-(int(x[2])-namugi)              
			n +=1                                                 # 이번달의 시작은 밑의 칸에서 시작
			
		n += b                                                    # 이번달 칸 추가
		
		if c != 0:                                                 #이번달 끝(나머지)이 있을때 칸 추가
			n+=1
			
		namugi = c

	print("Case #"+str(r+1)+": "+str(n))
	
