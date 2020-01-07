# 트리(Tree)

#### [트리의 정의]

: 노드(node)와 브랜치(branch)를 이용해서, 사이클을 이루지 않도록 구성한 데이터 구조

<br>

#### [트리의 용어]

- Node
- Root Node : 트리 맨위에 있는 노드
- Level : 최상위 노드를 level 0으로 가정하고, 연결된 노드의 깊이를 나타낸다.
- Parent Node
- Child Node
- Leaf Node
- Sibiling(Brother Node)
- Depth : 트리에서 Node가 가질 수 있는 최대 Level

<br>

#### [이진 트리]

: 노드의 최대 branch가 2인 트리

<br>

#### [이진 탐색 트리(BST)]

: 이진 트리 조건 + 트리내 **어떤 노드에서든 왼쪽에 있는 노드들은 작은값, 오른쪽에 있는 노드들은 큰값**이다.

  ([이진탐색 트리 gifs](https://www.mathwarehouse.com/programming/gifs/binary-search-tree.php))

<br>

#### [이진 탐색 트리의 장점과 주요 용도]

- 데이터 검색(탐색)에 주로 사용
- 탐색 속도 개선 가능
- 평균 시간 복잡도 : O(logn)
  - 균형 잡혀있지 않을때 최악의 시간 복잡도는 O(n) : 선형모양일때

<br>

----------------

#### [파이썬으로 트리 구현하기]

1. 노드 클래스 만들기

```python
class Node:
  def __init__(self, value):
  	self.value = value
  	self.left = None
  	self.right = None
```

<br>

2. 이진 탐색 트리에 데이터 삽입

```python
class NoneMgmt:
  def __init__(self, head):
  	self.head = head
  	
  def insert(self, value):  // 탐색후 올바른 위치에 value 삽입
  	self.current_node = self.head
  	while True:
  		if value < self.current_node:
            if self.left != None:
                self.current_node = self.current_node.left
            else:
                self.current_node.left = Node(value)    // 새로운 노드 생성
                break
        else:
            if self.current_node.right != None:
                self.current_node = self.current_node.right
            else:
                self.current_node.right = Node(value)
                break
```

<br>	3.  데이터 검색

```python
def search(self, value):
  self.current_node = self.head
  while self.current_node:
    if self.current_node == value;
      return True:
    elif value < self.current_node.value;
      self.current_node = self.current_node.left
    else:
      self.current_node = self.current_node.right
  return False:
```

​	<Br>

4. 데이터 삭제

```python
def delete(self, value):
	searched = False     // 해당 value가 트리내 존재 유무용
    self.current_node = self.head
    self.parent = self.head
    while self.current_node:
        if self.current_node.value == value:
            searched = True
            break
        elif value < self.current_node.value:
            self.parent = self.current_node
            self.current_node = self.current_node.left
        else:
            self.parent = self.current_node
            self.current_node = self.current_node.right
```



1) 자식 노드가 0개인 노드를 삭제하는 경우 (잎노드 삭제)

```python
	if self.current_node.left == None and self.current_node.right == None:
    	if value < self.parent.value:
            self.parent.left = None
        else:
            self.parent.right = None
        del self.current_node
```

2) 자식 노드가 1개인 노드를 삭제하는 경우

```python
# 해당 노드의 부모노드의 자식 노드를 현 노드의 자식노드로 지정한다.
	if self.current_node.left != None and self.current_node.right == None: # 왼쪽에 있을때
        if value < self.parent.value:
        	self.parent.left = self.current_node.left
    	else:
        	self.parent.right = self.current_node.left
   elif self.current_node.left == None and self.current_node.right != None # 오른쪽에 있을때
		if value < self.parent.value:
        	self.parent.left = self.current_node.right
        else:
            self.parent.right = self.current_node.right
```

3) **자식 노드가 2개인 노드를 삭제하는 경우**

```python
# case 3-1. 삭제할 노드의 오른 자식중 가장 작은 값(가장 왼쪽)을 가져옴
# case 3-2. 삭제할 노드의 왼쪽 자식중 가장 큰 값(가장 오른쪽)을 가져옴
# 이 두 방법중 한 방법을 사용한다.

	if self.current_node.left != None and self.current_node.right != None:
        if value < self.parent.value: #case 3-1
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:  # 순회(successor 찾기)
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
                
           	if self.chagne_node.right != None: # successor의 자식 노드 1개 있을때
                self.change_node_parent.left = self.change_node.right
            else:                              # successor의 자식 노드 없을때
            	self.change_node_parent.left = None
            # successor 노드의 위치를 바꿔줌    
            self.parent.left = self.change_node 
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
            
		else:
            self.change_node = self.current_node.right
            self.change_node_parent = self.current_node.right
            while self.change_node.left != None:
                self.change_node_parent = self.change_node
                self.change_node = self.change_node.left
            if self.change_node.right != None:
                self.change_node_parent.left = self.change_node.right
            else:
                self.change_node.parent.left = None
                
            self.parent.right = self.change_node 
            self.change_node.left = self.current_node.left
            self.change_node.right = self.current_node.right
	return True
```

<br>

5. 테스트 코드

   ```python
   # 0 - 999 숫자 중 임의로 100개 추출해 이진탐색트리에 입력, 검색, 삭제
   import random
   
   bst_num = set()
   while len(bst_num) != 100:
       bst_num.add(random.randint(0,999))
       
   # 삽입
   head = Nodee(500)  # 임의의 루트 노드 500
   binary_tree = NodeMgmt(head)
   for num in bst_nums:
       binary_tree.insert(num)
       
   # 검색  
   for num in bst_nums:
       if binary_tree.search(num) == False:
           print('search failed', num)
           
   # 랜덤 숫자 선택후 삭제
   delete_nums = set()
   bst_nums = list(bst_nums)
   while len(delete_nums) != 10:
       delete_nums.add(bst_nums(random.randint(0,99)))
       
   # 선택한 10개의 숫자를 삭제
   for del_num in delete_nums:
       if binary_tree.delete(del_num) == False:
           print('delete failed', del_num)
   ```

   

