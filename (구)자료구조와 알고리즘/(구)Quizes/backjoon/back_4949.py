import sys

def check(x):
    tmp = []
    for i in x:
        if i == '(' or i == '[':
            tmp.append(i)

        elif i == ')':
            if len(tmp) == 0 or tmp[len(tmp)-1] != '(':
            # if not tmp or tmp.pop() != '(' 이라 하면 중복작업 감소..
                return 'no'
            tmp.pop()

        elif i == ']':
            if len(tmp) == 0 or tmp[len(tmp)-1] != '[':
                return 'no'
            tmp.pop()

    if len(tmp)==0:
        return 'yes'
    else:
        return 'no'


x = sys.stdin.readline().rstrip()
while x != '.':
    print(check(x))
    x = sys.stdin.readline().rstrip()
