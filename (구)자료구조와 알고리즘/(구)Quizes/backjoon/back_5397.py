import sys
'''
for n in range(int(sys.stdin.readline().rstrip())):
    word=[]
    cursor = 0
    for i in sys.stdin.readline().rstrip():
        if i == "<":
            if cursor != 0:
                cursor-=1
        elif i == ">":
            if cursor != len(word):
                cursor+=1
        elif i =="-" and len(word) !=0:
            word.pop()
        else:
            word = word[:cursor]+[i]+word[cursor:]
            cursor+=1
    print(''.join(word))
'''

for _ in range(int(input())):
    left_stack = []
    right_stack = []
    for i in input():
        if i == '-':
            if left_stack:
                left_stack.pop()
        elif i == '<':
            if left_stack:
                right_stack.append(left_stack.pop())
        elif i == '>':
            if right_stack:
                left_stack.append(right_stack.pop())
        else:
            left_stack.append(i)
    left_stack.extend(reversed(right_stack))
    print(''.join(left_stack))
