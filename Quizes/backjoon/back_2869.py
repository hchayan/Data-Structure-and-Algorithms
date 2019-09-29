import sys

n = sys.stdin.readline().rstrip().split()

ans = (int(n[2]) - int(n[0]))/(int(n[0])-int(n[1]))+1
if ans != int(ans):
    ans +=1


print(int(ans))

'''
ex) 3 1 10 일때, 미끄러지기 전의 하루 최대 높이를 계산
3
3 + (3-1) = 5
7
9
11 <- 도착

이 규칙을 이용해 ans의 값을 지정
ex) ans = (10 - 3) / (3-1) + 1          #마지막 +1은 식의 맨 앞에서 초기 시작 값을 빼주엇고 이에 해당되는 날을 의미

그리고 값이 만약 정수가 아니면, 추가로 +1을 해줌으로써 해결
'''