#Latihan 5
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
    
    def display(self):
        print("\n Traversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def display_backward(self):
        def _display(node):
            if node is None:
                return
            _display(node.next)
            print(node.data, end=" -> ")
        
        print("\nTraversing backward:")
        _display(self.head)
        print("null")

# Contoh Penggunaan
print("===Tampilan 1===")
ll = LinkedList()
ll.insert_at_end(1)
ll.insert_at_end(2)
ll.insert_at_end(3)
ll.insert_at_end(4)
ll.insert_at_end(5)
ll.display()
ll.display_backward()
print()

print("===Tampilan 2===")
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)
ll.insert_at_end(40)
ll.display()
ll.display_backward()
print()

print("===Tampilan 3===")
ll = LinkedList()
ll.insert_at_end(7)
ll.display()
ll.display_backward()