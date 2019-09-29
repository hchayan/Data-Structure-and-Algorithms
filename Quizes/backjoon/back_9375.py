import sys

n = int(sys.stdin.readline().rstrip())

for nn in range(n):
    x = int(sys.stdin.readline().rstrip())
    tmp = {}
    for xx in range(x):
        i,j = sys.stdin.readline().rstrip().split()
        if j not in tmp.keys():
            tmp[j] = 1
        else:
            tmp[j]+=1
    ans = 0
    for i in range(1,len(tmp)+1):
        if i==1:
            ans+=sum(tmp.values())
        else:

'''
미해결)
조합을 이용해야함..
ex)
1 2 3
4
5 6
인경우

1개일때 : 6
2개일때 : 3*2+1*2+1*3 = 11
3개일때 " 3*2*1 = 6
답은 23
이것을 구현해야함..
'''
