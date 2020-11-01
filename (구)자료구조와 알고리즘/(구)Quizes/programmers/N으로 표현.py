# dp 문제 재귀형식까지만 품. (이거 이용해서



def find(N, number, exp, cnt):
    if eval(exp) == number:
        return cnt
    if cnt == 8:
        return 9
    return min(find(N, number, exp + str(N), cnt+1),
               find(N, number, exp + "+" + str(N), cnt+1),
               find(N, number, exp + "-" + str(N), cnt+1),
               find(N, number, exp + "*" + str(N), cnt+1),
               find(N, number, str(eval(exp)) + "*" + str(N), cnt + 1),
               find(N, number, exp + "/" + str(N), cnt+1),
               find(N, number, str(eval(exp)) + "/" + str(N), cnt + 1))




def solution(N, number):
    exp = str(N)
    return find(N, number, exp, 1)


for i in range(1,10):
    for num in range(1,10):
        print(i, num, solution(i, num))