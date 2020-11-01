
str = input()

tmp = ""
for i in range(0,len(str)):
    tmp+=str[i]
    if i%10==9:
        print(tmp)
        tmp=""
print(tmp)

