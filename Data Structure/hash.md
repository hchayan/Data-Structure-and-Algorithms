# 해시(hash)

: **임의의 길이**를 가지는 임의의 데이터에 대해 고**정된 길이의 데이터로 매핑**하는 함수

: 보안분야에서 사용(원래 문장 복호화 불가 특징)

<br>

#### [파이썬에서의 해시]

- 라이브러리 사용(hashlib)해서 해시 사용 가능

- 일반적으로 파이썬에서 해시는 **dict** 형을 의미한다.

- '값들의 모임'에서 특정 값을 찾는 코드를 구현할때,

   list로 구현하지마고, **set함수를 이용해 dict형태로 구현**하는데 더 효율적이다.

<br>

**# 예시 1) 라이브러리 해시**

```text
들어온 문자열의 SHA-256 해시값 구하기
```

```python
import hashlib

input_data = input()
encodata = input_data.encode()
res = hashlib.sha256(encodata).hexdigest()
print(res)
```

<br>

**# 예시2) dict 자료형**

```
datas = list(map(int, sys.stdin.readline().rstrip().split())) 보다
  #[5,2,1,3,4]
  
datas = set(map(int, sys.stdin.readline().strip().split())) 이 더 효율적
  #{1,2,3,4,5}
```

