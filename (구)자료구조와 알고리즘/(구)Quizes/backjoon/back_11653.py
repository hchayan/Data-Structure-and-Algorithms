import sys

x = int(sys.stdin.readline().rstrip())
'''
i = 2
def soin(x,i):
    if x==i:
        return i
    elif x%i==0:
        print(i)
        return soin(x//i, i)
    elif x%i !=0:
        return soin(x, i+1)
    return

print(soin(x,i))
'''

i = 2
while x >= i*i:
    if x%i == 0:
        print(i)
        x//=i
        continue
    i+=1
print(x)


