
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Method to display the maximum and minimum data in the single linked list.
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def get_max(self):
        if self.head is None:
            return None

        max_data = self.head.data
        current_node = self.head.next
        while current_node is not None:
            if current_node.data > max_data:
                max_data = current_node.data
            current_node = current_node.next

        return max_data

    def get_min(self):
        if self.head is None:
            return None

        min_data = self.head.data
        current_node = self.head.next
        while current_node is not None:
            if current_node.data < min_data:
                min_data = current_node.data
            current_node = current_node.next

        return min_data


linked_list = LinkedList()
for i in [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]:
    linked_list.insert(i)

linked_list.display()

print("Maximum data:", linked_list.get_max())
print("Minimum data:", linked_list.get_min())


# Method that converts the single linked list into a binary search tree. 
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next is not None:
            last_node = last_node.next

        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def to_bst(self, lst):
        if not lst:
            return None

        mid = len(lst) // 2
        root = Node(lst[mid])
        root.left = self.to_bst(lst[:mid])
        root.right = self.to_bst(lst[mid+1:])

        return root


linked_list = LinkedList()
for i in [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]:
    linked_list.insert(i)

linked_list.display()

lst = [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]
root = linked_list.to_bst(lst)

