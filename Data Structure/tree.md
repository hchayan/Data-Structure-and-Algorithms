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
- 탐색 속도 개선 가능 (logn 으로 일정)