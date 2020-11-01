# 하노이의 탑 원리
# n = 1일때 1->3
# n = 2일때 1->2, 1->3, 2->3
#.... 를 보면 규칙이 있다.

# 하노이의 탑 규칙 : n개의 원판 있을때, 우선 1에서 2로 n-1개의 원판들을 다 옮긴다.
# 그리고 n번째 원판을 1->3으로 옮긴다
# 마지막으로 2에서 3으로 n-1의 원판들을 다 옮긴다.

# 재귀의 법칙.. 재귀를 통해 n의 값을 점점 감소 시켜 n = 3일때 답, n = 2일때 답, n = 1일때 답.. 으로 구해서

# 우선 1->2로 n-1개의 원소를 다 옮겨야 하기 때문에 위 원리의 재귀를 from : 1, to : 2 를 기준으로 잡고 답을 구한다.
# 그리고 n 원반을 1->3으로 옮긴다 - print문
# 다시 위 재귀를 from :2 -> to : 3을 기준으로 답을 찾는다.


import sys

n = int(sys.stdin.readline().rstrip())

def hanoi(n, from_pos, tmp_pos, to_pos ):
    if n == 1:
        print(from_pos, to_pos)
        return
    else:
        hanoi(n-1, from_pos, to_pos, tmp_pos)
        print(from_pos, to_pos)
        hanoi(n-1, tmp_pos, from_pos, to_pos)

def cnt(n):
    if n == 1:
        return 1
    return cnt(n-1)+(2**(n-1))

print(cnt(n))
hanoi(n, '1', '2', '3')