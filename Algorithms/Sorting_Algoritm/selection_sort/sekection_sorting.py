# Selection Sorting

def change(x,i,j):             #배열 x의 i,j번째 원소를 상호 교환하는 함수
   x[i],x[j] = x[j],x[i]


def selectionSort(x):
  for i in range(len(x)):      # i는 비교할 배열내 범위의 시작 지점
    temp_min = i               # 초기 최소값은 x[i]로 지정
    for j in range(i,len(x)):  # (탐색범위 = i~len(x))
      if x[j] < x[temp_min]:   # 만약 탐색중에 해당 값이 지금까지 찾은 최소값보다 작으면
        temp_min = j           # 최소값을 새로이 지정

    change(x,temp_min,i)       # i 원소와 범위에서 찾은 최소값원소를 서로 위치 교환


x = [5,2,8,6,1,9,3,7]
selectionSort(x)
print(x)
