from typing import Any, Optional #Any — любой тип данных, Optional — может быть указанного типа или None

class Node: #Node для узла односвязного списка
    def __init__(self, value: Any, next_node: Optional['Node'] = None): #'Node' — форвард-декларация
        self.value = value #сохраняет значение в атрибуте узла
        self.next = next_node #сохраняет ссылку на следующий узел
    def __str__(self) -> str:
        return f"[{self.value}]" #Возвращает строку в формате [значение]

class SinglyLinkedList: #Создаёт класс для односвязного списка
    def __init__(self):
        self.head: Optional[Node] = None #ссылка на первый узел списка
        self.tail: Optional[Node] = None #ссылка на последний узел списка
        self._size: int = 0 #счётчик количества элементов
    def append(self, value: Any) -> None:
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            if self.tail is not None:  # Добавляем проверку
                self.tail.next = new_node
                self.tail = new_node
        self._size += 1
    def __str__(self) -> str:
        nodes = []
        current = self.head #начинаем с головы списка
        while current is not None:
            nodes.append(str(current)) #добавляем строковое представление текущего узла
            current = current.next
        nodes.append("None") #добавляем "None" в конец
        return " -> ".join(nodes) 
    def __repr__(self) -> str: #Метод repr для отладки и понятного представления объекта
        values = []
        current = self.head
        while current is not None:
            values.append(current.value)
            current = current.next
        return f"SinglyLinkedList({values})"
    def __len__(self) -> int: 
        return self._size #Возвращает значение счётчика _size

if __name__ == "__main__":
    lst = SinglyLinkedList() #создаёт пустой односвязный список
    lst.append(6)
    lst.append(1)
    lst.append(1.5)
    print(str(lst))
if __name__ == "__main__":
    lst = SinglyLinkedList()
    lst.append(6)
    lst.append(1)
    lst.append(1.5)
    print(str(lst))
    print(f"Длина списка: {len(lst)}")
    print(f"Репрезентация: {repr(lst)}")