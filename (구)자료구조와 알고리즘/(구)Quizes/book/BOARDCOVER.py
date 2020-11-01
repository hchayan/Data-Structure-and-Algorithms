# 종만북 - 완전탐색 - 게임판 덮기 - 6.5 - 난이도 하

# ===================== 주어지는 데이터 ====================
N = 3
H1, W1 = 3, 7
board1 = [
    ['#','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','#'],
    ['#','#','.','.','.','#','#'],
]

H2, W2 = 3, 7
board2 = [
    ['#','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','#'],
    ['#','#','.','.','#','#','#'],
]

H3, W3 = 8, 10
board3 = [
    ['#','#','#','#','#','#','#','#','#','#'],
    ['#','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','#'],
    ['#','.','.','.','.','.','.','.','.','#'],
    ['#','#','#','#','#','#','#','#','#','#'],
]
# ==============================================================

def boardCover(board):  # 주어진 board에 빈공간이 3의 배수가 아니면 0 리턴
    empty = 0
    for b in board:
        empty += b.count('.')
    if empty%3 != 0:
        return 0
    else:
        return countCase(board)

covers = [  # 왼쪽 위부터 탐색하다가 빈공간 (0,0)이 있으면 해당 빈공간 기준으로 중복 없이 만들수 있는 4가지 모양
    [[0,0], [0,1], [1,0]],  # r 모양
    [[0,0], [0,1], [1,1]],  # ㄱ 모양
    [[0,0], [1,0], [1,1]],  # ㄴ 모양
    [[0,0], [1,0], [1,-1]]  # J 모양
]
def countCase(board):
    # 재귀문 탈출 조건 : 내부에 빈공간 없으면 탈출
    flag = True
    for b in board:
        if b.count('.') != 0:
            flag = False
            break
    if flag:
        return 1

    # 주어진 board의 왼쪽 위부터 빈공간 찾기
    x, y = -1, -1   # 빈공간 정보
    for h in range(len(board)):
        for w in range(len(board[0])):
            if board[h][w] == ".":
                x = h
                y = w
                break
        if x > -1 and y > -1:
            break

    res = 0
    for cover in covers:
        # 영역 넘는경우 생략
        if x+max(cover[2][0],cover[1][0]) == len(board) or x+min(cover[2][0],cover[1][0]) < 0 or y + max(cover[2][1], cover[1][1]) == len(board[0]) or y + min(cover[2][1], cover[1][1]) < 0:
            continue

        if (board[x+cover[1][0]][y+cover[1][1]] == "." and board[x+cover[2][0]][y+cover[2][1]] == "."):
            board[x][y] = '#'
            board[x+cover[1][0]][y+cover[1][1]] = '#'
            board[x+cover[2][0]][y+cover[2][1]] = '#'
            res += countCase(board)
            board[x][y] = '.'
            board[x + cover[1][0]][y + cover[1][1]] = '.'
            board[x + cover[2][0]][y + cover[2][1]] = '.'



    return res



# ===============================================================
print(boardCover(board1))
print(boardCover(board2))
print(boardCover(board3))
