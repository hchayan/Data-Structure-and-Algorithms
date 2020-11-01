# Selection Sorting




def selection_sort(data):
  for i in range(len(data)):      # i는 비교할 배열내 범위의 시작 지점
    lowest = i             # 초기 최소값은 x[i]로 지정
    for j in range(i + 1,len(data)):  # (탐색범위 = i~len(x))
      if x[lowest] > x[j]:   # 만약 탐색중에 해당 값이 지금까지 찾은 최소값보다 작으면
        lowest = j           # 최소값을 새로이 지정

    data[lowest], data[i] = data[i], data[lowest]       # i 원소와 범위에서 찾은 최소값원소를 서로 위치 교환


x = [5,2,8,6,1,9,3,7]
selection_sort(x)
print(x)
