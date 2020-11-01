# 종만북 - 완전탐색 - 보글 게임 - p.150 - 난이도 하

# ===================== 주어지는 데이터 ====================
boggle = [
    ['U', ' R', 'L', 'P', 'M'],
    ['X', 'P', 'R', 'E' , 'T'],
    ['G', 'I', 'A', 'E', 'T'],
    ['X', 'T', 'N', 'Z', 'Y'],
    ['X', 'O', 'Q', 'R', 'S']
]

input1 = "PRETTY"
input2 = "GIRL"
input3 = "REPEAT"
# ==========================================================

def hasWord(y, x, word):
    if boggle[y][x] != word[0]:
        return False
    if len(word) == 1:
        return True

    dx = [-1, 0, 1, 1, 1, 0, -1, -1]
    dy = [-1, -1, -1, 0, 1, 1, 1, 0]
    for i in range(len(dx)):
        if y + dy[i] < 0 or y + dy[i] == len(boggle) or x + dx[i] < 0 or x + dx[i] == len(boggle[0]):
            continue
        if hasWord(y + dy[i], x + dx[i], word[1:]):
            return True
    return False

print(hasWord(1,1,input1))
print(hasWord(2,1,input2))