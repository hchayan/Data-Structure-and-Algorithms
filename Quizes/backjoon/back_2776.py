
for _ in range(int(input())):
    _1 = int(input())
    note1 = list(map(int, input().split()))
    note1.sort()

    _2 = int(input())
    note2 = list(map(int, input().split()))

    for note in note2:
        ans = 0
        start, end = 0, _1-1
        while start <= end:
            mid = (start+end)//2
            if note == note1[mid]:
                ans = 1
                break
            if note1[mid] > note:
                end = mid -1
            else:
                start = mid + 1

        print(ans)
