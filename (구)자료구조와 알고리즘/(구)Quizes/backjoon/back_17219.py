N, M = map(int, input().split())

password = {}

for i in range(N):
    key, value = input().split()
    password[key] = value

for i in range(M):
    print(password[input()])