def dailyTemperatures(T):
    ans = [0]*len(T)
    stack= []
    for i, num in enumerate(T):
        while stack and num > T[stack[-1]]:  # 현재 온도가 스택 값보다 높다면 정답 처리
            last = stack.pop()
            ans[last] = i - last
        stack.append(i)
    return ans


print(dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))