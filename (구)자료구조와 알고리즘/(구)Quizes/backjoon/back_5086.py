import sys

x = sys.stdin.readline().rstrip().split()

while x != ["0","0"]:
    if int(x[0])%int(x[1]) == 0:
        print("multiple")
    elif int(x[1])%int(x[0]) == 0:
        print("factor")
    else:
        print("neither")

    x = sys.stdin.readline().rstrip().split()


