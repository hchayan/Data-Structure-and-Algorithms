

n = int(input())
lis = set(map(int, input().split(" ")))
m = int(input())

for i in input().split(" "):
    if int(i) in lis:
        print("1")
    else:
        print("0")


