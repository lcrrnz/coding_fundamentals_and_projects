# Cree una estructura de objetos que asemeje un Double Ended Queue.
# Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
# Debe incluir un método para hacer `print` de toda la estructura.
# No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    data: str
    next: "Node"
    prevs: "Node"

    def __init__(self, data, next=None, prevs=None):
        self.data = data
        self.next = next
        self.prevs = prevs

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_left(self, data):
        new_top = Node(data)
        if self.head is None:
            self.head = self.tail = new_top
        else:
            new_top.next = self.head
            self.head.prevs = new_top
            self.head = new_top
        return new_top

    def push_right(self, data):
        new_tail = Node(data)
        if self.tail is None:
            self.head = self.tail = new_tail
        else:
            self.tail.next = new_tail
            new_tail.prevs = self.tail
            self.tail = new_tail
        return new_tail

    def pop_left(self):
        if self.head is None:
            print('Stack empty, left side')
            return None
        removed_top = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prevs = None
        return removed_top.data

    def pop_right(self):
        if self.tail is None:
            print('Stack empty, right side')
            return None
        removed_tail = self.tail
        self.tail = self.tail.prevs
        if self.tail is None:
            self.head = None
        else:
            self.tail.next = None
        return removed_tail.data
    
    def print_structure(self):
        current_top = self.head
        while current_top is not None:
            print(current_top.data)
            current_top = current_top.next


dq = Deque()
dq.push_left("A")
dq.push_right("B")
dq.push_left("C")
dq.push_right("D")
print("Initial structure:")
dq.print_structure()
print(f'Popped left: {dq.pop_left()}')
print(f'Popped right: {dq.pop_right()}')
print("After popping from both ends:")
dq.print_structure()
dq.push_left("X")
print(f'Added new item to the left:')
dq.print_structure()
dq.pop_left()
dq.pop_left()
dq.pop_left()
print(f'Once there are no items')
dq.pop_right()
dq.pop_left()