import sys

str = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline().rstrip())

cursor_pos = len(str)
for i in range(n):
    x = sys.stdin.readline().rstrip().split()

    if x[0] == "L":
        if cursor_pos !=0:
            cursor_pos-=1
    elif x[0] == "D":
        if cursor_pos != len(str):
            cursor_pos+=1
    elif x[0] =="B":
        if cursor_pos !=0:
            str = str[:cursor_pos-1]+str[cursor_pos:]
            cursor_pos-=1

    elif x[0] =="P":
        if cursor_pos !=0:
            str = str[:cursor_pos+1]+x[1]+str[cursor_pos+1:]
        else:
            str = x[1]+str
        cursor_pos+=1
print(str)