
pokemons = []
pokemons_num = {}

N, M = map(int,input().split())

for i in range(N):
    pk = input()
    pokemons.append(pk)
    pokemons_num[pk] = i + 1

for _ in range(M):
    item = input()
    if item.isdigit():
        print(pokemons[int(item)-1])
    else:
        print(pokemons_num[item])






