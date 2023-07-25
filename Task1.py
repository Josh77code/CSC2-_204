#Create a node class package nodes
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Create a single linked list class in package linkedlist

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode

    def insert(self, index, data):
        if index < 0 or index > self.getSize():
            raise IndexError("Index out of bounds")
        newNode = Node(data)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            newNode.next = current.next
            current.next = newNode

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next is not None:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            current = self.head
            while current is not None:
                print(current.data, end=" ")
                current = current.next

    def get(self, index):
        if index < 0 or index >= self.getSize():
            raise IndexError("Index out of bounds")
        current = self.head
        for i in range(index):
            current = current.next
        return current.data

    def getSize(self):
        size = 0
        current = self.head
        while current is not None:
            size += 1
            current = current.next
        return size

# Testing the linked list
if __name__ == "__main__":
    linkedList = SingleLinkedList()
    for i in [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]:
        linkedList.add(i)
    linkedList.display()