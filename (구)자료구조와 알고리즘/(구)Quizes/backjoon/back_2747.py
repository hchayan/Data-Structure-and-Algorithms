
n1, n2 = 0, 1

for i in range(int(input())):
    n1, n2 = n2, n1+n2
print(n1)



# 재귀 풀이 : 엄청난 시간 복잡도...
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)


print(fibonacci(int(input())))