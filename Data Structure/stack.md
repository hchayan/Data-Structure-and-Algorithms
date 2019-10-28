# 스택(Stack)

**: FILO**

<br>

#### [스택의 구현]

-----

##### 1. 파이썬 list형 사용해 스택 구현

```python
class Stack:
  def __init__(self):      # 스택 초기화
    self.list = []
    
  def push(self, list):    # 자료넣기
    self.list.append(x)
    
  def pop(self):           # 자료빼기
    return self.list.pop()

  def isEmpty(self):       # 스택 비어있은 여부 확인
    return not self.list()
```

<br>

##### 2. 연결리스트를 이용한 스택 구현

```python
class Node:
  def _init_(self, data):  # node data, next 초기값
    self.data = data
    self.next = None
    
class Stack:
 def _init_(self):         # stack node의 head 초기화
    self.head = None
 
 def push(self, data):     # data 넣기
    new_node = Node(data);
    nex_node.next = self.head
    self.head = new_node
    
 def pop(self):            # data 빼기(LIFO)
    if self.is_empty():
        return None
    del_data = self.head.data
    self.head = self.head.next
    return del_data
```



-------

#### [스택(Stack) 문제]

------

[백준 스택 문제 모음](https://www.acmicpc.net/problem/tag/%EC%8A%A4%ED%83%9D)

###### <백준>

| 번호 |                       문제                        |                    코드                     | 난이도 |    비고    |
| :--: | :-----------------------------------------------: | :-----------------------------------------: | :----: | :--------: |
|  1   | [스택 수열](https://www.acmicpc.net/problem/1874) | [python3](../Quizes/backjoon/back_1874.py)  |   하   |            |
|  2   |  [폭죽쇼](https://www.acmicpc.net/problem/1773)   | [python3](../Quizes/backjoon/back_1773.py)  |  최하  |            |
|  3   |  [키로커](https://www.acmicpc.net/problem/5397)   | [python3](../Quizes/backjoon/back_5397.py)  |   중   | 연결리스트 |
|  4   |    [탑](https://www.acmicpc.net/problem/2493)     |  [Pypy3](../Quizes/backjoon/back_2493.py)   |   하   |            |
|  5   |   [트럭](https://www.acmicpc.net/problem/13335)   | [python3](../Quizes/backjoon/back_13335.py) |   하   |            |

###### <프로그래머즈>

| 번호 |                             문제                             |                        코드                        | 난이도 | 비고 |
| :--: | :----------------------------------------------------------: | :------------------------------------------------: | :----: | :--: |
|  1   | [다리를 지나는 트럭](https://programmers.co.kr/learn/courses/30/lessons/42583) | [python3](../Quizes/programmers/truck_crossing.py) |   하   |      |
|  2   | [기능개발](https://programmers.co.kr/learn/courses/30/lessons/42586) |  [python3](../Quizes/programmers/function_dev.py)  |   하   |      |
|  3   | [주식가격](https://programmers.co.kr/learn/courses/30/lessons/42584) |  [python3](../Quizes/programmers/stock_price.py)   |   하   |      |

