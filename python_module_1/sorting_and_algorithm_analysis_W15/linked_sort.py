class Node:
    data : int
    next : "Node" 

    def __init__(self, data, next = None ):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head):
        self.head = head
        self.counter_changes = 0
        self.counter_iterations = 0
        self.made_change = None

    def sort_linked_list(self):
        if not self.head or not self.head.next:
            raise TypeError('Nodes are empty. Closing program')
        
        current_node = self.head
        while current_node:
            if not isinstance(current_node.data, (int, float)):
                raise TypeError(f'Invalid data type: {current_node.data} is not a number')
            current_node = current_node.next

        while True:
            self.counter_iterations += 1
            self.made_change = False
            prevs_node = None
            current_node = self.head
            while current_node and current_node.next:
                if current_node.data > current_node.next.data:
                    next_node = current_node.next
                    current_node.next = next_node.next
                    next_node.next = current_node
                    if prevs_node:
                        prevs_node.next = next_node
                    else:
                        self.head = next_node 
                    prevs_node = next_node
                    self.made_change = True
                    self.counter_changes += 1
                else:
                    prevs_node = current_node
                    current_node = current_node.next
            if not self.made_change:
                return
            

    def print_structure(self, label="Linked List Structure"):
        print(f"\n{label}:")
        current_node = self.head
        while current_node is not None:
            print(f'current node: {current_node.data}')
            current_node = current_node.next
        if self.counter_iterations > 0:
            print(f'\nThe list was iterated: {self.counter_iterations} times')
            if self.counter_changes > 0:
                print(f'The list items were changed: {self.counter_changes} times')
            else:
                print('The list was already sorted. No changes were needed.')


# test 1
n5 = Node(3)
n4 = Node(1, n5)
n3 = Node(5, n4)
n2 = Node(2, n3)
n1 = Node(4, n2)


ll = LinkedList(n1)
ll.print_structure()

ll.sort_linked_list()
ll.print_structure("Linked List Sorted Structure")


# # test 2
# n5 = Node(3)
# n4 = Node(1, n5)
# n3 = Node(5, n4)
# n2 = Node(2, n3)
# n1 = Node("Hola", n2)


# ll = LinkedList(n1)
# ll.print_structure()

# ll.sort_linked_list()
# ll.print_structure("Linked List Sorted Structure")

# test 3
# n5 = Node(3)
# n4 = Node(1, n5)
# n3 = Node(5, n4)
# n2 = Node(2, n3)
# n1 = Node(4, n2)


# ll = LinkedList(None)
# ll.print_structure()

# ll.sort_linked_list()
# ll.print_structure("Linked List Sorted Structure")

#do not modify, change nodes of place