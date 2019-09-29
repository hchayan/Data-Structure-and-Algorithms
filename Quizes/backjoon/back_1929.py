def isPrime(a, b):
    if b < 2:
        return []
    ans = []
    for x in range(a,b+1):
        flag = True
        for i in range(3,x,2):
            if x%i==0 or x%2==0:
                flag = False
                break
        if flag == True:
            ans.append(x)
    return ans




import sys

x = sys.stdin.readline().rstrip().split()

for i in isPrime(int(x[0]), int(x[1])):
    print(i)
