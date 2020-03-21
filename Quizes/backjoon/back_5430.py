# 하도 시간초과떠서 답 보니 C와 코드 같은데도 시간초과... Dp로 풀래..
# 이후 한참뒤에 푸는 방법 생각해냄. 그때그때 뒤집고 자르지말고 값으로 기록해둔뒤 한번에..
# 그래도 계속 오류...
# 아..
# 출력 양식을 str으로 해서 출력하니까 해결 ㅋㅋㅋㅋㅋㅋㅋ

for case in range(int(input())):
    func = list(input())
    length = int(input())
    nums = eval(input())

    flag = False
    rev = 0  # 현재 앞뒤 변경 여부
    front, back = 0, len(nums)   #잘라야 하는 위치

    for i in func:
        if i == 'R':
            rev += 1
        if i == 'D':
            if front > back-1:
                flag = True
                break

            if rev % 2 == 0:
                front += 1
            else:
                back -= 1

    if flag:
        print("error")
        continue

    nums = nums[front:back]
    if rev % 2 == 1:
        nums.reverse()

        # 출력함수
    print("[", end='')
    for i in range(len(nums)):
        if i == len(nums) - 1:
            print(nums[i], end='')
        else:
            print("%s," % (nums[i]), end='')
    print("]")





