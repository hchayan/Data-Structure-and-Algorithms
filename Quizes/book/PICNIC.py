# 종만북 - 완전탐색 - 소풍 - 6.3 - 난이도 하

# ===================== 주어지는 데이터 ====================
'''
3
2 1
0 1
4 6
0 1 1 2 2 3 3 0 0 2 1 3
6 10 0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5
'''
# ===========================================================
def countCase(taken):
    firstFree = -1    # 남은 학생들중 첫번째 학생 (중복카운트 제거위한 방법

    for i in range(len(taken)):
        if taken[i] == False:
            firstFree = i
            break

    if firstFree == -1:
        return 1


    #finish = True
    #for i in taken:
    #    if i == False:
    #        finish = False
    #        break
    #if finish:
    #    print("one")
    #    return 1


    res = 0   # 정답개수

    for i in range(firstFree+1, len(taken)):
        if taken[i] is False and relations[firstFree][i]:
            taken[firstFree] = taken[i] = True
            res += countCase(taken)
            taken[firstFree] = taken[i] = False  # 위에서 하위 문제로 taken 새로 줘서 재귀 했으니 새로운 재귀 위한 복귀

    #for i in range(len(taken)):
    #    for j in range(len(taken)):
    #       if not taken[i] and not taken[j] and relations[i][j]:
    #            taken[i] = taken[j] = True
    #            res += countCase(taken)
    #            taken[i] = taken[j] = False
    return res



# ==================== 결과 확인 코드 =========================
for N in range(int(input())):
    students, friends = map(int, input().split())
    case = list(map(int, input().split()))

    relations = []
    for i in range(students):
        relations.append([False]*students)

    for i in range(0, len(case), 2):
        relations[case[i]][case[i+1]] = True
        relations[case[i+1]][case[i]] = True

    print(countCase([False]*students))   # 짝지어진 학생 여부
