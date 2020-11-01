
# ans : 계산식, tmp : 현재 결과
def make_zero(N, ans):

    if N == 0:
        if ans[0] == "+":
            tmp = 0
            t = ""
            for i in range(len(ans)-1,0,-1):
                i = ans[i]
                if i == "+":
                    tmp += int(t)
                    t=""
                elif i == "-":
                    tmp -= int(t)
                    t=""
                elif i == " ":
                    continue
                else:
                    t = str(i) + t
            tmp += int(t)
            if tmp == 0:
                print(ans[1:])
        return
    make_zero(N - 1, "-" + str(N) + ans)
    make_zero(N - 1, " " + str(N) + ans)
    make_zero(N-1,  "+" + str(N) + ans)




import sys

for i in range(int(sys.stdin.readline().rstrip())):
    make_zero(int(sys.stdin.readline().rstrip()),"")
    print("")