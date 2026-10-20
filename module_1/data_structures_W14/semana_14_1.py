# Cree una estructura de objetos que asemeje un Stack.
# Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
# Debe incluir un método para hacer `print` de toda la estructura.
# No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Top:
    data: str
    next: "Top"

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Stack:
    head: Top
    def __init__(self, head):
        self.head = head

    def push (self, data):
        new_top = Top(data)
        new_top.next = self.head
        self.head = new_top

    def pop(self):
        if self.head is None:
            return None, print(f'stack empty')
        
        removed_top = self.head
        self.head = self.head.next
        return removed_top.data
    
    def print_structure(self):
        current_top = self.head
        while current_top is not None:
            print(current_top.data)
            current_top = current_top.next

first_top = Stack(Top("First value"))
first_top.push("Second value")
first_top.push("Third value")
first_top.print_structure()
print("\nremoving top\n")
first_top.pop()
first_top.print_structure()