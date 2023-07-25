# Algorithm to imp,ement binary search
def binary_search(arr, target):
    arr.sort()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

# Implementation of a  Queue data structure using a single linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front == None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear == None:
            self.front = new_node
            self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        temp = self.front
        self.front = temp.next
        if (self.front == None):
            self.rear = None

    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        while(temp != None):
            print(temp.data, end=" ")
            temp = temp.next

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.display()
queue.dequeue()
queue.dequeue()
queue.display()


