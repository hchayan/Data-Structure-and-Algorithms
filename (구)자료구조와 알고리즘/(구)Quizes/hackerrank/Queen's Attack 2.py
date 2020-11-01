
def queensAttack(n, k, r_q, c_q, obstacles):
    ans = 0


    for i in range(1, n+1):
        if [r_q + i, c_q] in obstacles or r_q + i > n:
            break
        ans +=1

    for i in range(1, n+1):
        if [r_q + i, c_q + i] in obstacles or r_q + i > n or c_q + i > n:
            break
        ans +=1

    for i in range(1, n + 1):
        if [r_q + i, c_q - i] in obstacles or r_q + i > n or c_q - i < 1:
            break
        ans += 1

    for i in range(1, n + 1):
        if [r_q, c_q - i] in obstacles or c_q - i < 1:
            break
        ans += 1

    for i in range(1, n + 1):
        if [r_q - i, c_q - i] in obstacles or r_q - i < 1 or c_q - i < 1:
            break
        ans += 1

    for i in range(1, n + 1):
        if [r_q - i, c_q] in obstacles or r_q - i < 1:
            break
        ans += 1

    for i in range(1, n + 1):
        if [r_q - i, c_q + i] in obstacles or r_q - i < 1 or c_q + i > n:
            break
        ans += 1

    for i in range(1, n + 1):
        if [r_q, c_q + i] in obstacles or c_q + i > n:
            break
        ans += 1

    return ans


print(queensAttack(5, 3, 4, 3, [[5,5], [4,2], [2,3]]))