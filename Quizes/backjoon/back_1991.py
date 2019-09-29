import sys


class Node:                             # 노드 양식 생성
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def search(node, key, node_left, node_right):    # 입력한 node 기준으로 key값 검색해 해당 node 있으면 해당 node의 left, right에 값 삽입
    if node is None:
        pass
    else:
        if node.data == key:
            insert_value(node, node_left, node_right)
        search(node.left, key,node_left, node_right)
        search(node.right, key,node_left, node_right)


def preorder(node):
    if node is None:
        return
    else:
        print(node.data, end="")
        preorder(node.left)
        preorder(node.right)


def inorder(node):
    if node is None:
        return
    else:
        inorder(node.left)
        print(node.data, end="")
        inorder(node.right)


def postorder(node):
    if node is None:
        return
    else:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end="")


def insert_value(node, node_left, node_right):  # node의 left, right 위치에 key이 '.'이 아니면 해당 값 삽입
    if  node_left != ".":
        node.left = Node(node_left)
    if node_right !=".":
        node.right = Node(node_right)


#====== main()

n = int(sys.stdin.readline().rstrip())

for i in range(n):
    node, node_left, node_right = sys.stdin.readline().rstrip().split()

    if i == 0:    # root 노드일때
        root = Node(node)
        insert_value(root, node_left, node_right)
    else:
        search(root, node, node_left, node_right)

preorder(root)
print("")
inorder(root)
print("")
postorder(root)

















