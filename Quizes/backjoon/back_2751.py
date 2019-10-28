import sys

n = int(sys.stdin.readline().rstrip())


ans = []
for i in range(n):
    ans.append(int(sys.stdin.readline().rstrip()))

for i in sorted(ans):  # 기본제공 정렬 함수
   print(i)



def Merge_Sort(A):
    if len(A) == 1:
        return A
    mid = len(A) // 2
    left = Merge_Sort(A[:mid])
    right = Merge_Sort(A[mid:])
    # Merge(A, p, q, r)
    array = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            array.append(right.pop(0))
        else:
            array.append(left.pop(0))
    if len(left) == 0:
        while len(right) > 0:
            array.append(right.pop(0))
    else:
        while len(left) > 0:
            array.append(left.pop(0))
    return array

print(Merge_Sort(ans))


