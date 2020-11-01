

def diagonalDifference(arr):
    a, b = 0, 0
    n = len(arr)
    for i in range(n):
        a += arr[i][i]
        b += arr[i][n-i-1]
    return abs(a-b)





arr = [[11, 2, 4],[4, 5, 6],[10, 8, -12]]
print(diagonalDifference(arr))