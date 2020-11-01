# 삽입 정렬(Insertion Sort) 알고리즘

- 자료 배열의 모든 요소를 앞에서부터 차례대로 정렬된 배열 부분과 비교해 자신의 위치 찾아 삽입
- 입력에 따라 수행시간 결정
- **평균 시간 복잡도 : O(n^2)**     
- 최선 시간 복잡도: O(n) / 최악 : O(n^2)


### 사용처
---
: 최악의 경우 O(n^2)를 가지는 기본 정렬 알고리즘중 하나이지만, 
 **데이터가 거의 정렬되어 있을때나 문제크기가 작을때(낮은 오버헤드)** 선택하는 알고리즘이다.

<br>

### 간단이론

----

**[선택 정렬 기본 구조]**

```python
for index in rnage(1, 데이터길이):
  for index2 in range(index-1, -1, -1):
    if 앞데이터 > 뒤데이터:
      swap(앞데이터, 뒤데이터)
```

**[선택 정렬 의사 코드]**

------

```
INSERTION-SORT(A)
  for j=2 to length[A]
    do key <- A[j]
      //A[j]를 정렬된 A[1:j-1] 배열에 삽입
      i = j-1
      while i> 0 and A[i] > key
      	A[i+1] = A[i]  //한칸 이동
      	i = i-1
      A[i+1] = key
```

**[삽입 정렬 예시]**

```
ex) list = [1,2,3,4,5] 일때,

12, 23, 12, 43, 32, 21, 54, 43, 32, 21 순으로 비교한다.
```

<br>

### 선택정렬 기본 구조 코드 (파이썬)

---
```python
def insertion_sort(data):
  for index in range(len(data) - 1):
    for index2 in range(index+1, 0, -1):
      if data[index2] < data[index2 - 1]:
        data[index2], data[index2 -1] = data[index2 - 1], data[index2]
      else:
        break
  return data
```

```python
def insertion_sort2(x):
  for size in range(1, len(x)):    # size : 비교할 배열의 범위
    val = x[size]                  # val : 비교할 원소
    i = size
    while i>0 and x[i-1] > val:    # 비교할 원소가 바로 앞의 원소보다 작고, 배열 범위내일 동안 실행
      x[i] = x[i-1]                # 앞의 원소와 위치 교환
      i-=1                         # 교환했으면 다음 앞에 있는 위치로 지정
    x[i] = val                     # 앞의 원소와 위치 교환2

  return x
```

