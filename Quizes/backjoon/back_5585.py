
quat = [500, 100, 50, 10, 5, 1]

bill = 1000 - int(input())

cnt, ans = 0, 0
while bill > 0 :
    if bill >= quat[cnt]:
        bill-=quat[cnt]
        ans+=1
    else:
        cnt+=1
print(ans)