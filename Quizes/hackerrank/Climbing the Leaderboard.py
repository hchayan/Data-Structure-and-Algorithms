
def climbingLeaderboard(scores, alice):
    scores += alice
    scores.sort(reverse=True)

    ans = []
    alice_cnt = len(alice)-1
    cnt = 1
    last = -1
    for i in range(len(scores)):
        if scores[i] == alice[alice_cnt]:
            ans = [cnt] + ans
            if alice_cnt > 0:
                alice_cnt-=1
            continue
        if scores[i] != last:
            cnt += 1

        last = scores[i]
    return ans





print(climbingLeaderboard([100, 90, 90, 80, 75, 60], [50, 65, 77, 90, 102]))
print(climbingLeaderboard([100, 100, 50, 40, 40, 20, 10], [5, 25, 50, 120]))