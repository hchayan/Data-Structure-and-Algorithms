import sys

for n in range(int(sys.stdin.readline().rstrip())):
    ans = []
    tmp = ''
    for x in sys.stdin.readline().rstrip():
        if x ==" ":
            ans.append(tmp)
            tmp = ''
        else:
            tmp = x + tmp
    ans.append(tmp)
    print(" ".join(ans))
