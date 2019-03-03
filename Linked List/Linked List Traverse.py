# 연결 리스트 구현하기

# 노드를 생성하는 클래스
class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

# 연결리스트 정의
class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

# 위치 반환
    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

# 순회
    def traverse(self):
        
        curr_node = self.head
        traversed_list = []
        
        while curr_node != None:
            curr_item = curr_node.data
            traversed_list.append(curr_item)
            curr_node = curr_node.next
            
        return traversed_list
