# 시간초과 되지만, 큐의 방식으로 구현
# 아니 큐 이용해서 풀어도 시간초과.. 야매로 공식 만들어서 풀어도 시간초과..
# 막판에 <, > 로 변환해주는거 까먹었었음
# 해결완료///
import sys

num, cnt = map(int,sys.stdin.readline().rstrip().split())

q = [n for n in range(1,num+1)]

ans = []

now = -1
for nn in range(num):

    if now+cnt > len(q)-1:
        now = (now+cnt)%len(q)
    else:
        now+=cnt

    ans.append(str(q.pop(now)))

    if now > 0:
        now-=1
    else:
        now+=len(q)-1

print("<"+", ".join(ans)+">")