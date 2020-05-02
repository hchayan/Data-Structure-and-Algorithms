N = int(input())

for i in range(1, 2*N-1, 2):
    print(' ' * ((2*N-i)//2) + i*'*')

for i in range(2*N-1, 0, -2):
    print(' ' * ((2 * N - i) // 2)+ i * '*')


