def insertion_sort(data):
  for index in range(len(data) - 1):
    for index2 in range(index+1, 0, -1):
      if data[index2] < data[index2 - 1]:
        data[index2], data[index2 -1] = data[index2 - 1], data[index2]
      else:
        break
  return data



def insertion_sort2(x):
  for size in range(1, len(x)):    # size : 비교할 배열의 범위
    val = x[size]                  # val : 비교할 원소
    i = size
    while i>0 and x[i-1] > val:    # 비교할 원소가 바로 앞의 원소보다 작고, 배열 범위내일 동안 실행
      x[i] = x[i-1]                # 앞의 원소와 위치 교환
      i-=1                         # 교환했으면 다음 앞에 있는 위치로 지정
    x[i] = val                     # 앞의 원소와 위치 교환2

  return x

x = [5,2,4,1,6,3]
print(insertion_sort(x))


