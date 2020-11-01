N = int(input())

for i in range(2*N-2, 0, -2):
    print('*' * ((2 * N - i) // 2)+ i * ' ' + '*' * ((2*N-i)//2))
for i in range(0, 2*N, 2):
    print('*' * ((2*N-i)//2) + i*' ' + '*' * ((2*N-i)//2))

