# 정렬시 sort 함수 쓰면 시간 복잡도 nlogn이라 지양해야한다..
# 그래서 애초에 dict 만들어줄때 dict 안에 a~z의 key값을 미리 넣어주고 value값들을 전부 0인 상태로 시작하는 방법을 하던가
# ord를 이용해 dict에서 5이상인거 꺼내 ans로 넣을때(이때 ans에 알파벳 개수 26자리에 0 넣어높기) ord 이용해서  계산해서 해당 알파벳 위치
# 에 값 넣어주던가.. 하면되는데 귀찮으니 생략




import sys

dic = {}
for i in range(int(sys.stdin.readline().rstrip())):
    x = sys.stdin.readline().rstrip()[0]
    if x not in dic:
        dic[x] = 1
    else:
        dic[x] +=1
print(dic)
ans = []
for i in dic.keys():
    if dic[i] >= 5:
        ans.append(i)

if len(ans) == 0:
    print("PREDAJA")
else:
    print(''.join(sorted(ans)))