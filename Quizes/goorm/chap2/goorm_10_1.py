# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
user_input = int(input())

lis = [0, 1]
for i in range(2, user_input + 1):
    lis.append((lis[i - 1] + lis[i - 2]) % (1000000007))

print(lis[user_input])