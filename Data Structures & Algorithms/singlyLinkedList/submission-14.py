class Node:

    def __init__(self, val):
        self.value = val
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        current = self.head
        if self.head is None:
            return -1
        for i in range(index):
            if current.next is None:
                return -1
            current = current.next
        return current.value

        

    def insertHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def insertTail(self, val: int) -> None:
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode

    def remove(self, index: int) -> bool:
        current = self.head
        previous = None
        if self.head is None:
            return False
        if index == 0:
            self.head = current.next
            return True
        for i in range(index):
            if current is None:
                return False
            previous = current
            current = current.next
        if current is None:
            return False
        previous.next = current.next
        return True

        

    def getValues(self) -> List[int]:
        values = []
        current = self.head
        while current != None:
            values.append(current.value)
            current = current.next
        return values
        
