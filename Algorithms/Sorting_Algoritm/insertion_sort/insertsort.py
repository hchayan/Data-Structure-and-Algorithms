def insert_sort(x):
  for size in range(1, len(x)):     # size : 비교할 배열의 범위
    val = x[size]                         # val : 비교할 원소
    i = size
    while i>0 and x[i-1] > val:    # 비교할 원소가 바로 앞의 원소보다 작고, 배열 범위내일 동안 실행
      x[i] = x[i-1]                        # 앞의 원소와 위치 교환
      i-=1                                  # 교환했으면 다음 앞에 있는 위치로 지정
    x[i] = val                              # 앞의 원소와 위치 교환2

  return x

x = [5,2,4,1,6,3]
print(insert_sort(x))