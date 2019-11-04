
for n in range(int(input())):
    ans = 0
    for i in input().split():
        if int(i)%2 == 1:
            ans += int(i)
    print("#"+str(n+1)+" "+str(ans))
