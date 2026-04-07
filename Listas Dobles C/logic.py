class ItemCompra:
    """
    Representa un articulo en la lista de compras (Nodo).
    """
    def __init__(self, name, detail, column="Sugerencias"):
        self.name = name
        self.detail = detail
        self.column = column 
        self.prev_item = None # Enlace al nodo anterior 
        self.next_item = None # Enlace al nodo siguiente 

class PurchaseLogic:
    """
    Gestiona la coleccion de articulos (Lista Doble).
    """
    def __init__(self):
        self.head = None # primera_tarea [cite: 19]
        self.tail = None # ultima_tarea [cite: 19]
        self.total = 0

    def is_empty(self):
        return self.head is None

    def add_item(self, name, detail, column="Sugerencias", to_front=False):
        # Permite agregar al inicio (Prioridad) o al final (Cola) [cite: 77, 81, 85]
        new_item = ItemCompra(name, detail, column)
        if self.is_empty():
            self.head = self.tail = new_item
        elif to_front:
            new_item.next_item = self.head
            self.head.prev_item = new_item
            self.head = new_item
        else:
            new_item.prev_item = self.tail
            self.tail.next_item = new_item
            self.tail = new_item
        self.total += 1

    def remove_item(self, name):
        # Eliminar articulo reconectando punteros [cite: 139, 151, 152]
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                if current.prev_item:
                    current.prev_item.next_item = current.next_item
                else:
                    self.head = current.next_item
                if current.next_item:
                    current.next_item.prev_item = current.prev_item
                else:
                    self.tail = current.prev_item
                self.total -= 1
                return True
            current = current.next_item
        return False

    def get_items(self):
        # Recorrido de Head a Tail [cite: 77, 89]
        items = []
        current = self.head
        while current:
            items.append(current)
            current = current.next_item
        return items

    def change_status(self, name, new_column):
        # Actualiza la columna del articulo
        current = self.head
        while current:
            if current.name.lower() == name.lower():
                current.column = new_column
                return True
            current = current.next_item
        return False