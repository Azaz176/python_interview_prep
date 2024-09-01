class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def delete_at_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        
        if self.head.next is None:  # Only one element in the list
            self.head = None
            return
        
        secondLast = self.head
        
        while secondLast.next.next:  # Check if the next of the next node exists
            secondLast = secondLast.next
        
        secondLast.next = None

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        
        if position <= 0:
            print("Position must be positive.")
            return
        
        current = self.head

        # Deleting the head node
        if position == 1:
            if current.next:
                self.head = current.next
                self.head.prev = None
            else:
                self.head = None
            current = None  # Free the node
            return
        
        # Traverse to the node at the given position
        for i in range(1, position):
            if current.next is None:
                print(f"Position {position} is out of bounds.")
                return
            current = current.next
        
        # Adjust pointers to bypass the current node
        if current.next:
            current.next.prev = current.prev
        
        if current.prev:
            current.prev.next = current.next
        
        # Free the current node
        current.next = None
        current.prev = None
        
    def search(self, key):
        current = self.head
        position = 1
        
        while current:
            if current.data == key:
                print(f"Element {key} found at position {position}")
                return current  # Return the node if found
            current = current.next
            position += 1
        
        print(f"Element {key} not found in the list.")
        return None  # Return None if not found



    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print()

# Example Usage
dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.display()  # Output: 10 20 30

dll.delete_at_end()
dll.display()  # Output: 10 20

dll.delete_at_end()
dll.display()  # Output: 10

dll.delete_at_end()
dll.display()  # Output: (empty line)















