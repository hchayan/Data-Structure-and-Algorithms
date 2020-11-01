# 연결 리스트(Linked list)

: 순차적으로 연결된 공간에 데이터를 나열하는 데이터 구조

: **크기 변경 가능, 여러가지 데이터 타입**만 저장가능(배열과 차이점)

: **떨어진 곳에 존재하는 데이터를 화살표로 연결해서 관리하는 데이터 구조**

  (C언에서 주요한 구조, 파이썬은 리스트 타입이 연결리스트 기능 제공)

<br>

#### [연결리스트 구현]

------

**1. 연결리스트의 Node 기본 구조 및 사용**

```python
class Node:
  def _init_(self, data):   
    self.data = data
    self.next = None
```

```
node1 = Node(1)
node2 = Node(2)
node1.next = node2
```

<br>

**2. 연결리스트 데이터 추가**

```python
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    
  def add(data):
    node = head
    while node.next:        # 마지막 노드까지 이동
        node = node.next
    node.next = Node(data)  # 마지막 노드의 next에 새로운 노드(데이터) 연결
```

```python
node1 = Node(1)
node2 = Node(2)
head = node1
for index in range(3, 10):
  add(index)
```

<br>

**3. 연결리스트 데이터 출력(검색)**

```python
node = head
while node.next:
  print(node.data)
  node = node.next
print(node.data)
```

<br>

**4. 연결리스트 데이터 관리(추가, 출력)**

```python
class NodeManage:
  def __init__(self, data):     # 생성자(값)으로 head 초기화
    self.head = Node(data)
    
  def add(self, data):          # 연결리스트에 data 넣기(맨끝에 삽입)
    if self.head == '':
        self.head = Node(data)
    else:
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data)
         
  def desc(self):               # 연결리스트의 값들 출력
    node = self.head
    while node:
        print(node.data)
        node = node.next
```

<br>

**5. 연결리스트 데이터 삭제**

- head(첫번째 노드)를 삭제하는 경우
- 마지막 노드를 삭제하는 경우
- 중간 노드를 삭제하는 경우

```python
...
  def delete(self, data):      # 연결리스트의 data값 노드 삭제
    if self.head == '':
      print ("해당 값을 가진 노드가 없습니다.")
      return
    
    if self.head.data = data:  # head가 data인 경우
        temp = self.head
        self.head = self.head.next
        del temp
    else:
        node = self.head
        while node.next: # node의 next가 있을때 반복
            if node.next.data == data:  # 순회중 찾은경우
                temp = node.next
                node.next = node.next.next  #마지막 노드면 node.next.next = None이므로 자동
                del temp
            else:
                node = node.next
                
```

<br>

<br>

------

#### [더블 링크드 리스트(double-linked list)]

: 기존 연결 리스트는 검색하는데 단일방향이기때문에 연결리스트 끝쪽에 위치해있으면 너무 오래걸림

: 내가 검색하고 싶은 노드가 앞쪽/뒤쪽에 있는지만 알면 좀더 빠르게 원하는 노드에 접근이 가능하다.

: **[이전데이터주소 | 데이터 | 다음데이터주소]**

<br>

**1. 더블 연결 리스트 노드 기본구조**

```python
class Node:
  def __init__(self, data, prev=None, next=None):
    self.prev = prev
    self.data = data
    self.next = next
```

<br>

**2. 더블 연결리스트 기본 연산(삽입, 출력)**

```python
class NodeMgmt:
  def __init__(self.data):
    self.head = Node(data)
    self.tail = self.head
    
  def insert(self, data):
    if self.head = None:            # head 없을때 주어진 data를 head, tail 노드로 설정
        self.head = Node(data)
        self.tail = self.head
    else:
        node = self.head
        while node.next:            # 리스트의 맨 마지막까지 이동
            node = node.next
        new = Node(data)
        node.next = new             # 주어진 data를 맨끝 node의 next값에 넣음
        new.prev = node             # 맨끝 node를 주어진 data node의 prev에 넣음
        self.tail = new             # tail값 주어진 data node로 재지정
        
  def desc(self):                   # 연결리스트내 노드들값 출력
    node = self.head
    while node:
        print(node.data)
        node = node.next
```

```python
double_linked_list = NodeMgmt(0)
for data in range(1,10):
  doublie_linked_list.insert(data)
double_linked_list.desc()
```

<br>

**3. 더블 연결리스트 검색**

```python
...
  def search_from_head(self, data):  # 더블 연결리스트 head 부터 검색
    if self.head == None:
      return False
    node = self.head
    while node:
      if node.data == data:
        return node
      else:
        node = node.next
    return False


  def search_from_tail(self, data):  # 더블 연결리스트 tail 부터 검색
    if self.tail = None:
        return False
    node = self.tail
    while node:
      if node.data == data:
        return node
      else:
        node = node.prev
    return False
```

<br>

**4. 더블 연결리스트 데이터 삽입**

```python
# 여기선 tail부터 node 검색하기에 before_data가 원래 연결리스트 순서대로보면 data 다음 노드이다.
#...
  def insert_before(self, data, before_data):#연결리스트내 before_data 노드 다음에 data 삽입
    if self.head == None:
        self.head = Node(data)
        return True
    else:
        node = self.tail
        while node.data != before_data:
          node = node.prev
          if node == None:          # 입력해준 직접 data를 찾지 못했을때
              return False
        new = Node(data)
        before_new = node.prev      # 삽입 앞뒤에 있는 node들간 쌍방향 연결(총 4번)
        before_new.next = new
        new.prev = before_new
        new.next = node
        node.prev = new
        
```

```python
double_linked_list.insert_before(1.5, 2)   # 0 1 1.5 2 3 4 5...
```

