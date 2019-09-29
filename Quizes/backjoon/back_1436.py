import sys

x = int(sys.stdin.readline().rstrip())

i = '665'
while x != 0:
    i = str(int(i)+1)
    if '666' in i:
        x-=1
print(i)