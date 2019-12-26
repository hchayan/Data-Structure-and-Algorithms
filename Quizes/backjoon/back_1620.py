
pokemons = {}

def find(data):


N, M = map(int,input().split())
for i in range(N):
    pokemons[i+1] = input()

pokemons.sort()
for i in range(M):
    item = input()
    if ord(item[0]) >= 48 and ord(item[0]) < 58:   # 숫자면
        print(pokemons[int(item)])
    else:
        print(find(item))




