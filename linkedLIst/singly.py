## Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

## Linked List definition
class LinkedList:
    def __init__(self):
        self.head = None

    ## Traversal in Linked List
    def traverse(self):
        current = self.head
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None")

    ## Insertion at the beginning
    def insertAtBeginning(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    ## Insertion at the end
    def insertAtEnd(self, data):
        newNode = Node(data)
        if self.head is None:  # Check if the list is empty
            self.head = newNode
            return
        last = self.head
        while last.next:  # Traverse to the last node
            last = last.next
        last.next = newNode

    ## Insertion at any position
    def insertAtAnyPosition(self, data, position):
        if position == 0:  # If inserting at the beginning
            self.insertAtBeginning(data)
            return
        
        current = self.head
        for i in range(position - 1):  # Traverse to the node before the target position
            if current is None:
                raise IndexError("Position out of bounds")
            current = current.next
        
        newNode = Node(data)
        newNode.next = current.next
        current.next = newNode

    ## Deletion at the beginning
    def deleteAtBeginning(self):
        if self.head is None:
            print("The list is empty, no node to delete.")
            return
        self.head = self.head.next

    ## Deletion at the end
    def deleteAtEnd(self):
        if self.head is None:
            print("The list is empty, no node to delete.")
            return
        if self.head.next is None:  # If there's only one node in the list
            self.head = None
            return
        second_last = self.head
        while second_last.next.next:  # Traverse to the second last node
            second_last = second_last.next
        second_last.next = None

    ## Deletion at any position
    ## Deletion at any position
    def deleteAtAnyPosition(self, position):
        if position == 0:  # If deleting the first node
            self.deleteAtBeginning()
            return
        
        prev = self.head
        
        # Check if the list is empty or if the first node is the only one
        if prev is None or prev.next is None:
            print("Position out of bounds")
            return

        current = self.head.next

        # Traverse the list to find the node to delete
        for i in range(position - 1):
            if current is None:  # If we reach the end before the position
                print("Position out of bounds")
                return
            prev = prev.next
            current = current.next

        if current is None:  # If the position is out of bounds
            print("Position out of bounds")
            return
        
        # Re-link the previous node to skip the current node
        prev.next = current.next
        current.next = None  # Optional: Clear the next pointer of the deleted node
    
    
    ## Searching a value in LL
    def searchForValue(self, value):
        current=self.head
        position=0
        while current:
            if current.data==value:
                return f"Value {value} found at position {position}."
            current=current.next
            position+=1
        return f"Value {value} not found in the list."


# Example Usage
linkedList = LinkedList()
linkedList.insertAtBeginning(1)
linkedList.insertAtEnd(2)
linkedList.insertAtEnd(3)
linkedList.insertAtEnd(4)

# Insert at the beginning
linkedList.insertAtBeginning(0)

# Insert at the end
linkedList.insertAtEnd(5)

# Insert at a specific position
linkedList.insertAtAnyPosition(99, 3)

# Traverse the linked list
linkedList.traverse()  # Output: 0->1->2->99->3->4->5->None

# Deletion examples:
linkedList.deleteAtBeginning()
linkedList.traverse()  # Output: 1->2->99->3->4->5->None

linkedList.deleteAtEnd()
linkedList.traverse()  # Output: 1->2->99->3->4->None

linkedList.deleteAtAnyPosition(2)
linkedList.traverse()  # Output: 1->2->3->4->None

print(linkedList.searchForValue(2))
print(linkedList.searchForValue(5))
