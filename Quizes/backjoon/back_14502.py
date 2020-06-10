# 완전탐색 연습용
import sys

N, M = map(int, sys.stdin.readline().split())

board = []
for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

print(board)

def spread(board):  # 주어진 board에서 병 퍼트리기

    for i in range(N*M):
        if board[i//N][i % N] == 2:
            toCheck = [[i // N + 1, i % N], [i // N - 1, i %
                                             N], [i // N, i % N+1], [i // N, i % N-1]]

            for t in toCheck:
                check = 0
                if board[t[0]][t[1]] == 0:
                    board[t[0]][t[1]] = 2
                    check += 1
                if check > 0:
                    spread(board)
                else:
                    res = 0
                    print(board)
                    for b in board:
                        res += b.count(0)
                    return res


ans = N*M+1
for i in range(N*M):
    for j in range(i+1, N*M):
        for k in range(j+1, N*M):
            if board[i//N][i % N] == 0 and board[j//N][j % N] == 0 and board[k//N][k % N] == 0:
                board[i//N][i % N], board[j//N][j %
                                                N], board[k//N][k % N] = 1, 1, 1
                print(spread(board))
                ans = min(ans, spread(board))
                board[i // N][i % N], board[j // N][j %
                                                    N], board[k // N][k % N] = 0, 0, 0

print(ans)