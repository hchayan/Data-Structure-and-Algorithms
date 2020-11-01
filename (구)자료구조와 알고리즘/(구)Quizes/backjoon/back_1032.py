
inputs = []

for i in range(int(input())):
    inputs.append(input())


ans = ''
for i in range(len(inputs[0])):
    tmp = inputs[0][i]
    for input in inputs:
        if tmp != input[i]:
            tmp = '?'
            break
    ans += tmp

print(ans)
