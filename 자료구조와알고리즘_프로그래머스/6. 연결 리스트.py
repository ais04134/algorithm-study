# Node 객체의 변수 값들이 data, next 이고 이 Node 값이 LinkedList의 변수로 들어가게 되는거다.
# 이게 어떤말인줄은 알겠는데 그럼 입력값을 어떤식으로 넣어주는거지 ?... 이거에 대한 이해가 아직 덜됬다!


class Node:
    def __init__(self, item):
        self.data = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None

    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None
        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def traverse(self):
        bins = [] # 빈 리스트 만들어줌
        curr = self.head # 헤드를 담아준다.
        while curr != None: # 헤드가 있는 동안
            bins.append(curr.data) # 데이터를 넣는다.
            curr = curr.next # 연결을 재정의한다.
        return bins # 리스트 출력한다.

a = Node(63)
b = Node(42)
c = Node(57)

L = [a, b, c]

d = LinkedList.traverse

print(d)