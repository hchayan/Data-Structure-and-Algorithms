# 선택 정렬 알고리즘

: 범위내 가장 작은 데이터를 찾아 가장 앞 데이터와 교환하는 알고리즘

<br>

### 간단이론

----

**[선택 정렬 기본 구조]**

```
for stand in range(데이터길이 - 1):
  lowest = stand
  for index in range(stand + 1 , 데이터길이):
    if 데이터[lowest] > 데이터[index]:
      lowest = index
  swap (lowest, stand)
```




```
ex) [5,2,8,6,1]

1. 배열 전체를 검사해 가장 작은 데이터 검색 (1)

2. 해당 원소를 배열의 첫번째 원소와 교환
=> [1,2,8,6,5]

3. 배열 2~n를 검사 반복.
```

<br>

### 선택정렬 기본 구조 코드 (파이썬)

---

```python
def selection_sort(data):                                                                 
  for i in range(len(data)):          # i는 비교할 배열내 범위의 시작 지점
    lowest = i                        # 초기 최소값은 x[i]로 지정                                   for j in range(i + 1,len(data)):  # (탐색범위 = i~len(x))                                     if x[lowest] > x[j]:   # 만약 탐색중에 해당 값이 지금까지 찾은 최소값보다 작으면           
          lowest = j           # 최소값을 새로이 지정                                         
      data[lowest], data[i] = data[i], data[lowest] 
                                                                                                             

x = [5,2,8,6,1,9,3,7]                                                                    
selection_sort(x)                                                                         
print(x)                                                                                 
```

