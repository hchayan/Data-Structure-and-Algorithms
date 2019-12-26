# 해시 테이블(Hash Table)

#### [해시 테이블]

----

: 키(key)에 데이터(valve)를 저장하는 데이터 구조

: 하지만 기존의 사전(dictionary)와 다른점은 key가 매핑될때, 해시함수에 의한 해시 키값으로 저장된다.

: **공간과 시간을 맞바꾸는 개념** : 해시테이블 공간 늘리면 충돌 가능성 감소 -> 작은 시간 복잡도

: **파이썬에서는 해쉬 별도 구현 필요X - 딕셔너리 타입 자체가 이미 해쉬이다**

<br>

#### [해시 테이블의 장단점과 주요 용도]

------

- 장점
  - 빠른 검색 속도(O(1))
  - 쉬운 중복 검사
- 단점
  - 많은 저장공간 필요 
  - 주소 충돌시 해결위한 자료구조 필요
- 주요 용도
  - **잦은 검색** 필요
  - **빈번한 저장, 삭제, 읽기** 필요 
  - 캐시 구현할때 (쉬운 중복 확인으로 인해)

<br>

#### [해시 테이블 구현]

----

1. 해시 테이블 만들기

   ```python
   hash_table = list([0 from i in range(10)])  //list를 사용해 hash_table 공간 생성
   hash_table
   ```

2. 해시 함수 만들기 (다양한 해시 함수중 Division 방법)

   ```python
   def hash_func(key):
   	return key % 5
   ```

3. **해시 테이블에 데이터 저장**

   ```python
   data1 = 'Andy'
   data2 = 'Dave'
   data3 = 'Trump'
   
   # ord() : 문자의 아스키 코드 리턴 함수
   print(ord(data1[0]),ord(data2[0]),ord(data3[0]))
   print(ord(data1[0]), hash_func(ord(data1[0])))
   ```

   ```python
   def storage_Data(data,value):  #data를 알맞은 해시 테이블 슬롯에 value 저장 함수
   	key = ord(data[0])
   	hash_adr = hash_func(key)
   	hash_table[hash_adr] = value
   ```

   ```python
   storgate_data('Andy','01055553333')  #데이터 해시위치에 value 저장
   ...
   ```

4. **해시 테이블에서 데이터 위치 value 출력**

   ```python
def get_data(data):  # data위치에 저장되어이 있는 value 출력
   	key = ord(data[0])
   	hash_adr = hash_func(key)
   	return hast_table[hash_adr]
   ```
   
   ```python
get_data('Andy')   # '01055553333' 출력
   ```
   

<br>

#### [+) 파이썬 hash 내장 함수]

------

```
hash(data)    # data에 따라 고정된 랜덤 해시값이 나온다(잘 사용되지 않는다.)
```

: 단 컴퓨터 on/off 마다 값이 달라질수도 있기에 잘 사용되지는 않는다.

<br>

#### [충돌 해결 알고리즘]

------

: 해시 테이블에 해시 함수로 인해 mapping될때 충돌하는 경우 해결하는 알고리즘.

1. **Chaining 기법**

   : 충돌 발생시, 연결 리스트 자료구조 사용해, 데이터 추가로 뒤에 연결시켜 저장하는 기법

   ```python
   # 문제 - 해시함수 : key%8, 해시 키 생성 : hash(data)일때, chaining 기법 구현
   
   hash_table = list([0 for i in range(8)])  #해시 테이블 크기 : 8
   
   def get_key(data):               # data에 대한 key(random)값 얻는 함수
       return hash(data)            # 해시 내장 함수
   
   def hash_function(key):          # data의 key값에 해당되는 해시 테이블 위치값 반환 해시 함수
       return key % 8
   
   def save_data(data, value):      # 해당 data의 해시 위치에 value를 저장()
       index = get_key(data)
       hash_adr = hash_function(get_key(data))
       
       if hash_table[hash_adr] != 0:
           for index in range(len(hash_table[hash_adr])):
               if hash_table[has_adr][index][0] == index_key:  # key값같은거있을때
                   hash_table[hash_adr][index][1] == value
                  	return
           hash_table[hash_adr].append([index.value])
       else:   # 슬롯에 값 처음 들어오면 해당 슬롯에 리스트 생성(연결리스트 대신)
           hash_table[hash_adr] = list([index.value])
   
       
   def read_data(data):
       index = get_key(data)
       hash_adr = hash_function(index)
       if hash_table[hash_adr] != 0  # 해당 슬롯에 data 있으면
         for index in range(len(hash_table[hash_adr])):
               if hash_table[hash_adr][index][0] == index:
                   return hash_table[hash_adr][index][1]
         return None
       else:
           return None
   ```

   

2. **Linear Probing 기법**

   : 충돌 발생시, 다음 address 부터 처음으로 나오는 빈공간에 저장하는 기법

#### [해시 테이블 문제]

------

| 번호 | 사이트 |       문제        |                     코드                      | 난이도 |      비고      |
| :--: | :----: | :---------------: | :-------------------------------------------: | :----: | :------------: |
|  1   |   -    | 간단한 해시테이블 | [python3](../Quizes/Etc/simple_hash_table.py) |   하   | 해시함수:key%8 |
