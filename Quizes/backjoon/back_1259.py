
n = input()

while n != '0':
    ans = 'yes'
    for i in range(len(n)//2+1):
        if n[i] != n[len(n)-i-1]:
            ans = 'no'
            break
    print(ans)
    n = input()