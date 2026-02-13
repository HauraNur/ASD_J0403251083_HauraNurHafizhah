#Latihan 1
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

    def delete_node(self,key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return
        
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:
            return
        
        prev.next = temp.next
        temp = None
    
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

# Contoh Penggunaan
ll = LinkedList()
ll.insert_at_end(3)
ll.insert_at_end(5)
ll.insert_at_end(13)
ll.insert_at_end(2)
ll.delete_node(13)
ll.display()

#Latihan 3
class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None #Menyimpan node terakhir untuk traversing mundur
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
           self.tail.next = new_node
           new_node.prev = self.tail
           self.tail = new_node

    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return
    
    def display_forward(self):
        print("\nTraversing forward:")
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")
    
    def display_backward(self):
        print("\nTraversing backward:")
        temp = self.tail
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.prev
        print("null")

# Contoh Penggunaan
dll = DoublyLinkedList()
dll.insert_at_end(2)
dll.insert_at_end(6)
dll.insert_at_end(9)
dll.insert_at_end(14)
dll.insert_at_end(20)
dll.display_forward()
dll.display_backward()
print()
print(dll.search(9))
print()

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