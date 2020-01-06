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

#### [해시 테이블의 시간복잡도]

- 일반적인 경우(충돌 없는경우) : O(1)
- 최악의 경우(충돌이 매번 발생) : O(n)
- 해시 테이블의 경우, 일반적인 경우를 기대하고 만들기 때문에, **시간 복잡도는 O(1)**이라고 할 수 있다.

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
           hash_table[hash_adr].append([index, value])
       else:   # 슬롯에 값 처음 들어오면 해당 슬롯에 리스트 생성(연결리스트 대신)
           hash_table[hash_adr] = list([index, value])
   
       
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

   <br>

2. **Linear Probing 기법**

   : 충돌 발생시, 다음 address 부터 처음으로 나오는 빈공간에 저장하는 기법중 하나
   
   : h(k, i) = h(k) + i 
   
   ```python
   # 문제 - 해시함수 : key%8, 해시 키 생성 : hash(data)일때, linear probing 기법 구현
   
   hash_table = list([0 for i in range(8)])  #해시 테이블 크기 : 8
   
   def get_key(data):              
       return hash(data)            
   
   def hash_function(key):        
       return key % 8
   
   def save_data(data, value):
       index_key = get_key(data)
       hash_address = hash_function(index_key)
       if hash_table[hash_address] != 0:
           # 현재 들어가는 곳부터 해시테이블 끝까지
           for index in range(hash_address, len(hash_table)):  # linear probing
               if hash_table[index] == None:   # 해당 슬롯에 데이터 없으면
                   hash_table[index] = [index_key, value]
                  	return
               # key가 동일한 데이터가 있을때, 해당 데이터를 지나가는게아니라 업데이터 해줘야 한다.
               elif hash_table[index][0] == index_key:  
                   hash_table[index][1] = value
                   return
       else:
           hash_table[hash_address] = [index_key, value]
           
   def read_data(data):  
       index_key = get_key(data)
       hash_address = hash_function(index_key)
       
       if hash_table[hash_address] != 0:
           for index in range(hash_address, len(hash_table)):
               if hash_table[index] == 0: # 원하는 키값 찾지못했는데 비어있는 슬롯 발견했을때
                   return None
               elif hash_table[index] == index_key:  # 원하는 키값일때
                   return hash_table[index][1]
       else:  # 데이터 없을때
           return None
   ```
   
   <br>
   
 3. **빈번한 충돌을 개선하는 기법**

    : 빈번한 충돌 발생하면 위와같이 반복문 사용해서 순회해야 해서 효율성이 떨어진다.

    : 그래서 해시 테이블은 **충돌을 최대한 줄이는게** 주요 목표이며 사용 목적이다.

    - 해시 테이블의 슬롯을 n배 증가 시키는 방법  ( ex. 8 -> 16 )  

      : 그만큼 공간과 탐색 시간 교환

    - **해시 함수와 키 생성 함수 : 해시 함수 실행할때마다 달라지는 값**

      - SHA 

        : 유명한 안전한 해시 알고리즘 (SHA-256 : 블록체인에서 주로 사용)

        : **고정된 길이의 16진수 값을 리턴**해주기에 해시 함수로 유용하게 사용할 수 있다.

    <br>

    1) **SHA-1**

    ```python
    import hashlib
    
    # 인코딩 : 바이트로 변환 : 주어진 data를 byte형태로 풀어준후 해시함수에 넣어준다
    data = 'test'.encode()   
    hash_object = hashlib.shal()
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()   # 추출할때 16진수로 추출
    print(hex_dig) # 'text'라는 값에 대한 해시함수 적용한 값을 16진수로 출력한 형태
    ```

    2) **SHA-256**

    ```python
    import hashlib
    
    data = 'test'.encode()   
    hash_object = hashlib.sha256()  # SHA-256
    hash_object.update(data)
    hex_dig = hash_object.hexdigest()  
    print(hex_dig)
    ```

    3) **위의 chaining 기법 적용한 코드에 키 생성 함수를 sha256 해시 알고리즘을 사용하도록 변경하기**

    ```python
    import hashlib
    
    hash_table = list([0 for i in range(8)])  
    
    def get_key(data):  # SHA-256 방식             
        hash_object = hashlib.sha256()
        hash_object.update(data.encode())
        hex_dig = hash_object.hexdigest()
        return int(hex_dig, 16) # 16진수를 10진수로 변환(아래서 %8로 key 정하기때문에 int형 필요)
    
    def hash_function(key):        
        return key % 8
    
    def save_data(data, value):    
        index = get_key(data)
        hash_adr = hash_function(get_key(data))
        
        if hash_table[hash_adr] != 0:
            for index in range(len(hash_table[hash_adr])):
                if hash_table[has_adr][index][0] == index_key:  
                    hash_table[hash_adr][index][1] == value
                   	return
            hash_table[hash_adr].append([index, value])
        else:  
            hash_table[hash_adr] = list([index, value])
    
        
    def read_data(data):
        index = get_key(data)
        hash_adr = hash_function(index)
        if hash_table[hash_adr] != 0 
          for index in range(len(hash_table[hash_adr])):
                if hash_table[hash_adr][index][0] == index:
                    return hash_table[hash_adr][index][1]
          return None
        else:
            return None
    ```

    

    



#### [해시 테이블 문제]

------

| 번호 | 사이트 |       문제        |                     코드                      | 난이도 |      비고      |
| :--: | :----: | :---------------: | :-------------------------------------------: | :----: | :------------: |
|  1   |   -    | 간단한 해시테이블 | [python3](../Quizes/Etc/simple_hash_table.py) |   하   | 해시함수:key%8 |

