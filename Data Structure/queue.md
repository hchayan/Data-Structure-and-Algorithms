# 큐(Queue)

: FIFO

: 멀티 태스킹을 위한 프로세스 스케줄링 방식을 구현하기 위하 주로 사용(우선순위 큐등)

<br>

#### [스택의 구현]

------

**1. 파이썬 list사용해 큐 구현**

```python
class Queue:  
    def __init__(self):        # 큐 초기화    
        self.qu = []  
        
    def enqueue(self, qu):      # 자료 넣기(enqueue)    
        self.qu.append(x)  
        
    def dequeue(self):          # 자료 빼기(dequeue)    
        return self.qu.pop(0)  
    
    def isEmpty(self):         # 큐 내용 여부 확인    
        return not self.qu()
```

**2. 큐 라이브러리 사용해서 구현**

```python
import queue

q = queue.Queue()
q.put(x)        # 자료 넣기
q.get()         # 자료 꺼내기
q.qsize()       # q내 데이터 개수
```

**3. 우선순위 큐 구현(tuple 형태 큐)**

```python
import queue

q = queue.PriorityQueue()

q.put((10, "korea"))  # 숫자 작을수록 높은 우선순위
q.put((5, 1))
q.put((15, "china"))

q.get()  # 우선순위 높은거부터 출력(작은 숫자)
```



-------

#### [데크 자료구조]

: 양쪽 끝에서 삽입과 삭제가 모두 이루어지는 자료구조

 

**# 데크 자료구조 종류**

```
1) scroll(입력 제한 데크) : 삽입이 한쪽에서만 일어나는 데크
2) self(출력 제한 데크) : 삭제가 한쪽에서만 일어나는 데크
```



**1. 스택과 큐를 혼합해 데크 구현**

```python
q = list()

def enqueue(data):
  q.append(data)

def dequeue():
  data = q[0]    #데크의 왼쪽 데이터 추출
  del q[0]
  return data
```

**2. 라이브러리를 이용해 데크 구현(collection)**

```python
from collections 
import dequed

q = deque(x)       # 데크 초기화
from i in dq;  
  print(i, end='')  # 데크내 문장 출력

dq.append(x)        # 데크의 오른쪽에 자료 삽입
dq.appendleft(x)    # 데크의 왼쪽에 자료 삽입
dq.pop()            # 데크 자료 빼기
dq.popleft()
dq.extend(x)        # 데크에 한번에 삽입
dq.extendleft(x)
```

<br>

------

#### 큐(Queue) 문제

------

[백준 큐 문제 모음](https://www.acmicpc.net/problem/tag/%ED%81%90)

| 번호 | 사이트 |                       문제                        |                    코드                    | 난이도 |              비고               |
| :--: | :----: | :-----------------------------------------------: | :----------------------------------------: | :----: | :-----------------------------: |
|  1   |  백준  | [프린터 큐](https://www.acmicpc.net/problem/1966) | [python3](../Quizes/backjoon/back_1996.py) |   하   |                                 |
|  2   |  백준  |    [AC](https://www.acmicpc.net/problem/5430)     | [python3](../Quizes/backjoon/back_5430.py) |  중하  | 덱. 값으로 계산후 한번에 자르기 |

