# Калантарян Мери 
# Лабараторная работа 10

## linked_list.py
```
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
```
## structures.py
```
from collections import deque #deque нужен для эффективной реализации очереди

class Stack: #Стек — структура данных LIFO
    def __init__(self):
        self._data = [] #_data — приватный атрибут
    def push(self, item): #push — добавляет элемент на вершину стека
        self._data.append(item) #добавляет элемент в конец списка
    def pop(self):
        if self.is_empty():
            raise IndexError
        return self._data.pop() #удаляет последний элемент списка и возвращает его
    def peek(self): #смотрит верхний элемент без удаления
        if self.is_empty():
            return None
        return self._data[-1] #обращение к последнему элементу списка
    def is_empty(self):
        return len(self._data) == 0
    def __len__(self): #вызывается при использовании len(obj)
        return len(self._data)
    def __str__(self): #при преобразовании объекта в строку
        return f"Stack({self._data})" #Возвращает строку вида Stack([элементы])

class Queue: #Очередь — структура данных FIFO
    def __init__(self):
        self._data = deque() #создаёт пустую двустороннюю очередь
    def enqueue(self, item): #добавляет элемент в конец очереди
        self._data.append(item) #добавляет элемент в правый конец deque
    def dequeue(self): #удаляет и возвращает элемент из начала очереди
        if self.is_empty():
            raise IndexError
        return self._data.popleft() # удаляет элемент с левого конца deque
    def peek(self): 
        if self.is_empty():
            return None
        return self._data[0] #обращение к первому элементу deque
    def is_empty(self):
        return len(self._data) == 0
    def __len__(self):
        return len(self._data)
    def __str__(self): #Преобразует deque в список для красивого отображения
        return f"Queue({list(self._data)})"

if __name__ == "__main__":
    s = Stack() #Демонстрация стека
    s.push(10)
    s.push(20)
    s.push(30)
    print(s)
    print(f"peek: {s.peek()}")
    print(f"pop: {s.pop()}")
    print(s)
    print() 
    q = Queue() #Демонстрация очереди
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(q)
    print(f"peek: {q.peek()}")
    print(f"dequeue: {q.dequeue()}")
    print(q)
if __name__ == "__main__":
    # Демонстрация Stack
    print("=" * 40)
    print("ДЕМОНСТРАЦИЯ STACK:")
    print("=" * 40)
    
    s = Stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"Стек после добавления элементов: {s}")
    print(f"Верхний элемент (peek): {s.peek()}")
    print(f"Извлекаем элемент (pop): {s.pop()}")
    print(f"Стек после извлечения: {s}")
    print(f"Стек пуст? {s.is_empty()}")
    print(f"Количество элементов: {len(s)}")
    
    print("\n" + "=" * 40)
    print("ДЕМОНСТРАЦИЯ QUEUE:")
    print("=" * 40)
    
    q = Queue()
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print(f"Очередь после добавления элементов: {q}")
    print(f"Первый элемент (peek): {q.peek()}")
    print(f"Извлекаем элемент (dequeue): {q.dequeue()}")
    print(f"Очередь после извлечения: {q}")
    print(f"Очередь пуста? {q.is_empty()}")
    print(f"Количество элементов: {len(q)}")
```
![](images/A/lab10/1.png)
# Лабараторная работа 9 

## group.py
```
import csv
from pathlib import Path
from typing import List, Optional


class Student:
    """Класс студента для хранения данных"""
    
    def __init__(self, fio: str, group: str, age: int, gpa: float):
        self.fio = fio
        self.group = group
        self.age = age
        self.gpa = gpa
    
    def __repr__(self):
        return f"Студент: {self.fio}, Группа: {self.group}, Возраст: {self.age}, GPA: {self.gpa:.2f}"
    
    def to_dict(self):
        """Преобразует объект студента в словарь для CSV"""
        return {
            'fio': self.fio,
            'group': self.group,
            'age': str(self.age),
            'gpa': str(self.gpa)
        }


class Group:
    """Класс для управления группой студентов с CRUD-операциями"""
    
    HEADER = ['fio', 'group', 'age', 'gpa']
    
    def __init__(self, storage_path: str):
        """
        Инициализация группы с путем к CSV-файлу
        
        Args:
            storage_path: путь к CSV-файлу для хранения данных
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Создает файл с заголовком, если он не существует"""
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, 'w', encoding='utf-8', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=self.HEADER)
                writer.writeheader()
    
    def _read_all(self) -> List[dict]:
        """
        Читает все записи из CSV-файла
        
        Returns:
            Список словарей с данными студентов
        """
        students = []
        with open(self.path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(row)
        return students
    
    def _write_all(self, students: List[dict]):
        """
        Записывает все записи в CSV-файл
        
        Args:
            students: список словарей с данными студентов
        """
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
            writer.writerows(students)
    
    def _dict_to_student(self, data: dict) -> Student:
        """
        Преобразует словарь в объект Student
        
        Args:
            data: словарь с данными студента
            
        Returns:
            Объект Student
        """
        return Student(
            fio=data['fio'],
            group=data['group'],
            age=int(data['age']),
            gpa=float(data['gpa'])
        )
    
    def list(self) -> List[Student]:
        """
        Возвращает всех студентов в виде списка объектов Student
        
        Returns:
            Список объектов Student
        """
        data = self._read_all()
        return [self._dict_to_student(row) for row in data]
    
    def add(self, student: Student):
        """
        Добавляет нового студента в CSV
        
        Args:
            student: объект Student для добавления
        """
        # Проверяем, существует ли уже студент с таким ФИО
        existing = self.find(student.fio)
        if existing:
            raise ValueError(f"Студент с ФИО '{student.fio}' уже существует")
        
        # Добавляем нового студента
        data = self._read_all()
        data.append(student.to_dict())
        self._write_all(data)
    
    def find(self, substr: str) -> List[Student]:
        """
        Ищет студентов по подстроке в ФИО
        
        Args:
            substr: подстрока для поиска в ФИО
            
        Returns:
            Список найденных студентов
        """
        data = self._read_all()
        found = [row for row in data if substr.lower() in row['fio'].lower()]
        return [self._dict_to_student(row) for row in found]
    
    def remove(self, fio: str) -> bool:
        """
        Удаляет запись(и) с данным ФИО
        
        Args:
            fio: ФИО студента для удаления
            
        Returns:
            True если студент был удален, False если не найден
        """
        data = self._read_all()
        original_count = len(data)
        
        # Удаляем все записи с указанным ФИО
        data = [row for row in data if row['fio'] != fio]
        
        if len(data) < original_count:
            self._write_all(data)
            return True
        return False
    
    def update(self, fio: str, **fields) -> bool:
        """
        Обновляет поля существующего студента
        
        Args:
            fio: ФИО студента для обновления
            **fields: поля для обновления (fio, group, age, gpa)
            
        Returns:
            True если студент был обновлен, False если не найден
        """
        data = self._read_all()
        updated = False
        
        for row in data:
            if row['fio'] == fio:
                # Обновляем указанные поля
                for key, value in fields.items():
                    if key in self.HEADER:
                        if key in ['age', 'gpa']:
                            row[key] = str(value)
                        else:
                            row[key] = value
                updated = True
                break
        
        if updated:
            self._write_all(data)
        
        return updated
    
    def stats(self) -> dict:
        """
        Собирает статистику по студентам
        
        Returns:
            Словарь со статистикой
        """
        students = self.list()
        
        if not students:
            return {
                "count": 0,
                "avg_gpa": None,
                "groups": {}
            }
        
        # Основная статистика
        gpa_values = [student.gpa for student in students]
        
        # Статистика по группам
        groups = {}
        for student in students:
            groups[student.group] = groups.get(student.group, 0) + 1
        
        return {
            "count": len(students),
            "avg_gpa": sum(gpa_values) / len(gpa_values),
            "groups": groups
        }
    
    def clear(self):
        """Очищает все записи, оставляя только заголовок"""
        with open(self.path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.HEADER)
            writer.writeheader()
```
![](images/A/lab09/1.png)
![](images/A/lab09/2.png)
![](images/A/lab09/3.png)
# Лабараторная работа 8

## models.py
```
from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Self
import re


@dataclass
class Student:
    """Класс для представления студента."""
    
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self) -> None:
        """Валидация данных после инициализации."""
        # Валидация ФИО
        if not self.fio or not isinstance(self.fio, str):
            raise ValueError("ФИО должно быть непустой строкой")
        
        # Валидация формата даты (YYYY-MM-DD)
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD")
        
        # Валидация группы
        if not self.group or not isinstance(self.group, str):
            raise ValueError("Название группы должно быть непустой строкой")
        
        # Валидация среднего балла
        if not isinstance(self.gpa, (int, float)):
            raise ValueError("Средний балл должен быть числом")
        if not 0 <= self.gpa <= 5:
            raise ValueError(f"Средний балл должен быть в диапазоне 0-5, получено: {self.gpa}")
    
    def age(self) -> int:
        """Возвращает количество полных лет студента."""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        # Вычисляем разницу в годах
        age_years = today.year - birth_date.year
        
        # Корректируем, если день рождения в этом году ещё не наступил
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1
            
        return age_years
    
    def to_dict(self) -> dict:
        """Сериализует объект Student в словарь."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """Десериализует объект Student из словаря."""
        # Проверяем обязательные поля
        required_fields = ["fio", "birthdate", "group", "gpa"]
        for field_name in required_fields:
            if field_name not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field_name}")
        
        # Создаем объект Student
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"])
        )
    
    def __str__(self) -> str:
        """Возвращает строковое представление студента."""
        return (f"Студент: {self.fio}\n"
                f"Группа: {self.group}\n"
                f"Дата рождения: {self.birthdate} (Возраст: {self.age()} лет)\n"
                f"Средний балл: {self.gpa:.2f}")
    
    def __repr__(self) -> str:
        """Возвращает официальное строковое представление."""
        return (f"Student(fio='{self.fio}', birthdate='{self.birthdate}', "
                f"group='{self.group}', gpa={self.gpa})")
```
## serialize.py
```
import json
from typing import List
from pathlib import Path
from .models import Student


def students_to_json(students: List[Student], path: str) -> None:
    """
    Сохраняет список студентов в JSON-файл.
    
    Args:
        students: Список объектов Student
        path: Путь к файлу для сохранения
    """
    # Преобразуем студентов в словари
    data = [student.to_dict() for student in students]
    
    # Создаем директорию, если она не существует
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Сохраняем в JSON
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"Данные успешно сохранены в {path}")


def students_from_json(path: str) -> List[Student]:
    """
    Загружает список студентов из JSON-файла.
    
    Args:
        path: Путь к JSON-файлу
        
    Returns:
        List[Student]: Список объектов Student
    """
    file_path = Path(path)
    
    if not file_path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    
    # Читаем JSON
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Преобразуем словари в объекты Student
    students = []
    for item in data:
        try:
            student = Student.from_dict(item)
            students.append(student)
        except (ValueError, KeyError) as e:
            print(f"Ошибка при создании студента из данных {item}: {e}")
            continue
    
    print(f"Загружено {len(students)} студентов из {path}")
    return students
```

![](images/A/lab08/image.png)

# Лабараторная работа 7 

## test_json_csv
```
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


class TestJsonToCsv:
    """Тесты для функции json_to_csv"""

    def test_json_to_csv_basic(self, tmp_path: Path):
        """Тест базовой конвертации JSON в CSV"""
        src = tmp_path / "test.json"
        dst = tmp_path / "test.csv"

        data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
            {"name": "Charlie", "age": 35, "city": "Kazan"},
        ]

        src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        json_to_csv(str(src), str(dst))

        # Проверяем, что файл создан
        assert dst.exists()

        # Проверяем содержимое CSV
        with dst.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 3
        assert set(rows[0].keys()) == {"name", "age", "city"}
        assert rows[0]["name"] == "Alice"
        assert rows[0]["age"] == "25"

    def test_json_to_csv_different_keys(self, tmp_path: Path):
        """Тест с объектами, имеющими разные ключи"""
        src = tmp_path / "test.json"
        dst = tmp_path / "test.csv"

        data = [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "city": "SPb"},  # Нет age
            {"name": "Charlie", "age": 35, "country": "Russia"},  # Дополнительный ключ
        ]

        src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        json_to_csv(str(src), str(dst))

        with dst.open(encoding="utf-8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 3
        # Все возможные ключи должны быть в заголовках
        assert set(rows[0].keys()) == {"name", "age", "city", "country"}

    def test_json_to_csv_file_not_found(self):
        """Тест на несуществующий файл"""
        with pytest.raises(FileNotFoundError):
            json_to_csv("nonexistent.json", "output.csv")

    def test_json_to_csv_invalid_json(self, tmp_path: Path):
        """Тест на некорректный JSON"""
        src = tmp_path / "invalid.json"
        dst = tmp_path / "test.csv"

        src.write_text("{ invalid json }", encoding="utf-8")

        with pytest.raises(ValueError):
            json_to_csv(str(src), str(dst))

    def test_json_to_csv_empty_json(self, tmp_path: Path):
        """Тест на пустой JSON - должен вызывать ошибку"""
        src = tmp_path / "empty.json"
        dst = tmp_path / "test.csv"

        src.write_text("[]", encoding="utf-8")

        # Ожидаем ValueError для пустого JSON
        with pytest.raises(ValueError, match="JSON файл пустой"):
            json_to_csv(str(src), str(dst))

        # Убеждаемся, что CSV файл не создан
        assert not dst.exists()


class TestCsvToJson:
    """Тесты для функции csv_to_json"""

    def test_csv_to_json_basic(self, tmp_path: Path):
        """Тест базовой конвертации CSV в JSON"""
        src = tmp_path / "test.csv"
        dst = tmp_path / "test.json"

        csv_content = """name,age,city
Alice,25,Moscow
Bob,30,SPb
Charlie,35,Kazan"""

        src.write_text(csv_content, encoding="utf-8")
        csv_to_json(str(src), str(dst))

        # Проверяем, что файл создан
        assert dst.exists()

        # Проверяем содержимое JSON
        with dst.open(encoding="utf-8") as f:
            data = json.load(f)

        assert len(data) == 3
        assert data[0] == {"name": "Alice", "age": "25", "city": "Moscow"}
        assert data[1] == {"name": "Bob", "age": "30", "city": "SPb"}

    def test_csv_to_json_empty_values(self, tmp_path: Path):
        """Тест с пустыми значениями в CSV"""
        src = tmp_path / "test.csv"
        dst = tmp_path / "test.json"

        csv_content = """name,age,city
Alice,25,Moscow
Bob,,SPb
Charlie,35,"""

        src.write_text(csv_content, encoding="utf-8")
        csv_to_json(str(src), str(dst))

        with dst.open(encoding="utf-8") as f:
            data = json.load(f)

        assert data[1] == {"name": "Bob", "age": "", "city": "SPb"}
        assert data[2] == {"name": "Charlie", "age": "35", "city": ""}

    def test_csv_to_json_file_not_found(self):
        """Тест на несуществующий файл"""
        with pytest.raises(FileNotFoundError):
            csv_to_json("nonexistent.csv", "output.json")

    def test_csv_to_json_empty_csv(self, tmp_path: Path):
        """Тест на пустой CSV"""
        src = tmp_path / "empty.csv"
        dst = tmp_path / "test.json"

        src.write_text("", encoding="utf-8")

        with pytest.raises(ValueError):
            csv_to_json(str(src), str(dst))


class TestRoundTrip:
    """Тесты на полный цикл конвертации"""

    def test_json_csv_json_roundtrip(self, tmp_path: Path):
        """Тест полного цикла JSON -> CSV -> JSON"""
        original_json = tmp_path / "original.json"
        intermediate_csv = tmp_path / "intermediate.csv"
        final_json = tmp_path / "final.json"

        original_data = [
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
        ]

        # Сохраняем оригинальный JSON
        original_json.write_text(
            json.dumps(original_data, ensure_ascii=False), encoding="utf-8"
        )

        # Конвертируем JSON -> CSV
        json_to_csv(str(original_json), str(intermediate_csv))

        # Конвертируем CSV -> JSON
        csv_to_json(str(intermediate_csv), str(final_json))

        # Читаем результат
        with final_json.open(encoding="utf-8") as f:
            final_data = json.load(f)

        # Проверяем, что данные сохранились (возраст будет строкой после конвертации)
        assert len(final_data) == len(original_data)
        assert final_data[0]["name"] == original_data[0]["name"]
        assert final_data[0]["age"] == str(original_data[0]["age"])  # Число -> строка
        assert final_data[0]["city"] == original_data[0]["city"]
```
## test_text
```
import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    """Тесты для функции normalize"""

    @pytest.mark.parametrize(
        "source, expected",
        [
            ("ПрИвЕт\nМИр\t", "привет мир"),
            ("ёжик, Ёлка", "ежик, елка"),
            ("Hello\r\nWorld", "hello world"),
            ("  двойные   пробелы  ", "двойные пробелы"),
            ("", ""),
            ("   ", ""),
            ("ТЕСТ!!!", "тест!!!"),
            ("Много\t\t\tтабов", "много табов"),
        ],
    )
    def test_normalize_basic(self, source, expected):
        assert normalize(source) == expected


class TestTokenize:
    """Тесты для функции tokenize"""

    @pytest.mark.parametrize(
        "source, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello world test", ["hello", "world", "test"]),
            ("один, два. три!", ["один", "два", "три"]),
            ("", []),
            ("   ", []),
            ("только-только", ["только-только"]),
            ("раз     много     пробелов", ["раз", "много", "пробелов"]),
        ],
    )
    def test_tokenize_basic(self, source, expected):
        assert tokenize(source) == expected


class TestCountFreq:
    """Тесты для функции count_freq"""

    def test_count_freq_basic(self):
        tokens = ["я", "люблю", "python", "я", "python", "python"]
        result = count_freq(tokens)
        expected = {"я": 2, "люблю": 1, "python": 3}
        assert result == expected

    def test_count_freq_empty(self):
        assert count_freq([]) == {}

    def test_count_freq_case_sensitive(self):
        tokens = ["Word", "word", "WORD"]
        result = count_freq(tokens)
        # Предполагаем, что токены уже нормализованы
        assert result == {"Word": 1, "word": 1, "WORD": 1}


class TestTopN:
    """Тесты для функции top_n"""

    def test_top_n_basic(self):
        freq = {"a": 5, "b": 10, "c": 3, "d": 7}
        result = top_n(freq, 2)
        expected = [("b", 10), ("d", 7)]
        assert result == expected

    def test_top_n_tie_breaker(self):
        # Тест на случай одинаковой частоты (должна быть алфавитная сортировка)
        freq = {"z": 5, "a": 5, "m": 5, "b": 10}
        result = top_n(freq, 3)
        # b с самой высокой частотой, затем a, m, z с одинаковой частотой
        # но в алфавитном порядке: a, m, z
        expected = [("b", 10), ("a", 5), ("m", 5)]
        assert result == expected

    def test_top_n_more_than_available(self):
        freq = {"a": 1, "b": 2}
        result = top_n(freq, 5)
        expected = [("b", 2), ("a", 1)]
        assert result == expected

    def test_top_n_empty(self):
        assert top_n({}, 5) == []

    def test_top_n_zero(self):
        freq = {"a": 1, "b": 2}
        assert top_n(freq, 0) == []


class TestIntegration:
    """Интеграционные тесты для всего пайплайна"""

    def test_full_pipeline(self):
        text = "Привет мир! Мир привет всем. Всем привет еще раз."
        normalized = normalize(text)
        tokens = tokenize(normalized)
        freq = count_freq(tokens)
        top_words = top_n(freq, 2)

        assert normalized == "привет мир! мир привет всем. всем привет еще раз."
        assert "привет" in tokens
        assert "мир" in tokens
        assert freq["привет"] == 3
        assert freq["мир"] == 2
        assert top_words[0][0] == "привет"
```
## pyproject
```
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[tool.black]
line-length = 88
target-version = ['py38']
include = '\.pyi?$'
extend-exclude = '''
/(
  # directories
  \.eggs
  | \.git
  | \.hg
  | \.mypy_cache
  | \.tox
  | \.venv
  | build
  | dist
)/
'''

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = ["test_*.py"]
python_classes = ["Test*"]
python_functions = ["test_*"]
addopts = [
    "--strict-markers",
    "--strict-config",
    "--verbose"
]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests as integration tests"
]

[tool.coverage.run]
source = ["src"]
omit = [
    "*/test_*",
    "*/__pycache__/*"
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "if self.debug:",
    "if settings.DEBUG",
    "raise AssertionError",
    "raise NotImplementedError",
    "if 0:",
    "if __name__ == .__main__.:",
    "class .*\\bProtocol\\):",
    "@(abc\\.)?abstractmethod"
]
```
![](images/A/lab07/проверкастиля.png)
![](images/A/lab07/с.png)
![](images/A/lab07/BUM.png)
![](images/A/lab07/pytest.png)

# Лабараторная работа  6 

## cli_convert
```
import argparse # для обработки аргументов командной строки
from pathlib import Path 
import sys


def check_file_exists(path_str: str):
    path = Path(path_str)
    if not path.exists():
        print(f"Ошибка: входной файл '{path}' не найден.", file=sys.stderr)
        sys.exit(1)
    return path

def json2csv(input_path: str, output_path: str):
    check_file_exists(input_path)
    print(f"[demo] Конвертация JSON → CSV: {input_path} → {output_path}")
    # json_to_csv(input_path, output_path)


def csv2json(input_path: str, output_path: str):
    check_file_exists(input_path)
    print(f"[demo] Конвертация CSV → JSON: {input_path} → {output_path}")
    # csv_to_json(input_path, output_path)


def csv2xlsx(input_path: str, output_path: str):
    check_file_exists(input_path)
    print(f"[demo] Конвертация CSV → XLSX: {input_path} → {output_path}")
    # csv_to_xlsx(input_path, output_path)


def main():
    parser = argparse.ArgumentParser(description="CLI-конвертеры данных (ЛР6)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    # ---- json2csv ----
    p1 = sub.add_parser("json2csv", help="Преобразовать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON-файл")
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV-файл")

    # ---- csv2json ----
    p2 = sub.add_parser("csv2json", help="Преобразовать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON-файл")

    # ---- csv2xlsx ----
    p3 = sub.add_parser("csv2xlsx", help="Преобразовать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX-файл")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        json2csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv2json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv2xlsx(args.input, args.output)
if __name__ == "__main__":
    main()
```
![](images/A/lab06/stats.png)

## cli_text


```

import argparse
from pathlib import Path
import sys



def cat_command(input_path: str, numbered: bool = False):
    """Вывод содержимого файла построчно"""
    path = Path(input_path)
    if not path.exists():
        print(f"Ошибка: файл '{input_path}' не найден.", file=sys.stderr)
        sys.exit(1)

    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if numbered:
                print(f"{i:4d}: {line.rstrip()}")
            else:
                print(line.rstrip())


def stats_command(input_path: str, top_n: int = 5):
    """Простейший анализ частот слов (упрощённо, если нет lab03)"""
    path = Path(input_path)
    if not path.exists():
        print(f"Ошибка: файл '{input_path}' не найден.", file=sys.stderr)
        sys.exit(1)

    with path.open(encoding="utf-8") as f:
        text = f.read().lower()

    words = [w.strip(".,!?;:\"'()[]") for w in text.split()]
    freq = {}
    for w in words:
        if not w:
            continue
        freq[w] = freq.get(w, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]

    print(f"Топ {top_n} слов в '{input_path}':")
    for word, count in sorted_items:
        print(f"{word:15s} {count}")


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для анализа текста (cat, stats)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ---- cat ----
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # ---- stats ----
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
if __name__ == "__main__":
    main()

```
![](images/A/lab06/cat.png)



# Лабараторная работа 5 

## csv_xlsx
```
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """CSV → XLSX"""
    cpath = Path(csv_path)
    if not cpath.exists():
        raise FileNotFoundError(f"Нет файла: {csv_path}")

    with cpath.open(encoding="utf-8") as f:
        rows = list(csv.reader(f))
    if not rows:
        raise ValueError("Пустой CSV")

    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    for row in rows:
        ws.append(row)

    # Автоширина
    for col in ws.columns:
        length = max(len(str(cell.value or "")) for cell in col)
        ws.column_dimensions[get_column_letter(col[0].column)].width = max(8, length + 2)

    wb.save(xlsx_path)


if __name__ == "__main__":
    csv_to_xlsx("data/samples/cities.csv", "data/out/cities.xlsx")
    csv_to_xlsx("data/samples/people.csv", "data/out/people.xlsx")
```
## json_csv
```
 # src/lab05/json_csv.py
import json
import csv
from pathlib import Path


def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    json_file = Path(json_path)
    csv_file = Path(csv_path)
    
    if not json_file.exists():
        raise FileNotFoundError(f"JSON файл не найден: {json_path}")
    
    if json_file.suffix.lower() != '.json':
        raise ValueError(f"Неверный тип файла: ожидается .json, получен {json_file.suffix}")
    
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")
    
    if not data:
        raise ValueError("JSON файл пустой")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")
    
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    fieldnames = sorted(all_fields)
    
    try:
        with open(csv_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for row in data:
                complete_row = {field: str(row.get(field, '')) for field in fieldnames}
                writer.writerow(complete_row)
                
    except Exception as e:
        raise ValueError(f"Ошибка записи CSV: {e}")


def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_file = Path(csv_path)
    json_file = Path(json_path)
    
    if not csv_file.exists():
        raise FileNotFoundError(f"CSV файл не найден: {csv_path}")
    
    if csv_file.suffix.lower() != '.csv':
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}")
    
    try:
        with open(csv_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            
            if not fieldnames:
                raise ValueError("CSV файл не содержит заголовка")
            
            rows = list(reader)
            
    except Exception as e:
        raise ValueError(f"Ошибка чтения CSV: {e}")
    
    if not rows:
        raise ValueError("CSV файл пустой (нет данных, только возможный заголовок)")
    
    data = []
    for row in rows:
        string_row = {key: str(value) if value is not None else '' for key, value in row.items()}
        data.append(string_row)
    
    try:
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")
    




    # пример использования
if __name__ == "__main__":
    # JSON -> CSV
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
    
    # CSV -> JSON  
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
```
## Входные данные 
```
# data/samples/cities.csv
city,population,area_km2,foundation_year
Москва,12678079,2561,1147
Санкт-Петербург,5398064,1439,1703
Казань,1257341,614,1005
Новосибирск,1625631,502,1893
```
```
# data/samples/people.csv
name,age,city,profession,salary
Алексей,25,Москва,Инженер,
Мария,30,Санкт-Петербург,,80000
Иван,28,Казань,Разработчик,90000
```
```
[
  {
    "name": "Алексей",
    "age": 25,
    "city": "Москва",
    "profession": "Инженер"
  },
  {
    "name": "Мария",
    "age": 30,
    "city": "Санкт-Петербург",
    "salary": 80000
  },
  {
    "name": "Иван",
    "age": 28,
    "city": "Казань",
    "profession": "Разработчик",
    "salary": 90000
  }
]
```
## Вывод 
![](images/A/lab05/cvs=>json.png)
![](images/A/lab05/json=>cvs.png)



# Лабараторная работа 4 

## io_txt_csv
```
import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path, 'r', encoding=encoding) as file:
        return file.read()

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if rows:
        first_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидается {first_len}")
    ensure_parent_dir(path)
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)

def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
```
## text_report
```
import re
import argparse
from pathlib import Path
from io_txt_csv import read_text, write_csv

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=text.replace('\n',' ').replace('\t',' ').replace('\r',' ')
    while '  ' in text:
        text=text.replace('  ',' ')
    text=text.strip()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    if casefold:
        text=text.casefold()
    return text



def tokenize(text: str) -> list[str]:
    text=''.join(char for char in text if char.isalpha()\
    or char.isspace() or char == '-' or char in '0123456789')
    text=text.split()
    return text

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] =1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))#получаем пары слов,сорт(по уб,по вз)
    return sorted_items[:n]



def main():
    parser = argparse.ArgumentParser(description='Анализ текста и создание отчета')
    parser.add_argument('--in', dest='input_file', default='data/lab04/input.txt',
                       help='Входной текстовый файл (по умолчанию: data/lab04/input.txt)')
    parser.add_argument('--out', dest='output_file', default='data/lab04/report.csv',
                       help='Выходной CSV файл (по умолчанию: data/lab04/report.csv)')
    parser.add_argument('--encoding', default='utf-8',
                       help='Кодировка файла (по умолчанию: utf-8, для Windows: cp1251)')
    args = parser.parse_args()
    
    try:
        print(f"Чтение файла: {args.input_file}")
        text = read_text(args.input_file, encoding=args.encoding)
        print("Анализ текста...")
        normalized = normalize(text)
        tokens = tokenize(normalized)
        word_counts = count_freq(tokens)
        sorted_words = sorted(word_counts.items(), 
                             key=lambda x: (-x[1], x[0]))
        print(f"Сохранение отчета: {args.output_file}")
        rows = [(word, count) for word, count in sorted_words]
        header = ("word", "count")
        write_csv(rows, args.output_file, header)
        print("\n--- ОТЧЕТ ---")
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(word_counts)}")
        print("Топ-5:")
        freq = count_freq(tokens)
        top_words = top_n(freq, 5)
        for word, count in top_words:
            print(f"{word}:{count}")
        print(f"\nОтчет сохранен в: {args.output_file}")
        
    except FileNotFoundError:
        return 'FileNotFoundError'
    except UnicodeDecodeError:
        return 'UnicodeDecodeError'
    except Exception:
        return 'Exception'

if __name__ == "__main__":
    main()
```


# Лабараторная работа 3

## Задание А 
## А1
```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=text.replace('\n',' ').replace('\t',' ').replace('\r',' ')
    while '  ' in text:
        text=text.replace('  ',' ')
    text=text.strip()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    if casefold:
        text=text.casefold()
    return text

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```
![](images/A/lab03/A1.png)

## A2
```
def tokenize(text: str) -> list[str]:
    text=''.join(char for char in text if char.isalpha()\
    or char.isspace() or char == '-' or char in '0123456789')
    text=text.split()
    return text
print(tokenize("привет мир"))
print(tokenize("hello, world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
![](images/A/lab03/A2.png)

## A3
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] =1
    return freq

tokens1 = ["a","b","a","c","b","a"]
freq1 = count_freq(tokens1)
tokens2 = ["bb","aa","bb","aa","cc"]
freq2 = count_freq(tokens2)

print(f"Токены {tokens1} → частоты {freq1}")
print(f"Токены {tokens2} → частоты {freq2}")
```
![](images/A/lab03/A3.png)

## A4
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] =1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))#получаем пары слов,сорт(по уб,по вз)
    return sorted_items[:n]

tokens1 = ["a","b","a","c","b","a"]
freq1 = count_freq(tokens1)
tokens2 = ["bb","aa","bb","aa","cc"]
freq2 = count_freq(tokens2)

print(f"top_n(..., n=2) → {top_n(freq1, 2)}")
print(f"top_n(..., n=2) → {top_n(freq2, 2)}")
```
![](images/A/lab03/A4.png)

## Задание В
```
import sys
import os
from lib import text as txt

def main():
    text = input()
    normalized_text = txt.normalize(text, casefold=True, yo2e=True)
    tokens = txt.tokenize(normalized_text)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    freq = txt.count_freq(tokens)
    top_words = txt.top_n(freq, 5)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")
```
    ![](images/A/lab03/B.png)


# Лабараторная работа 2 

## Задание A
## A1
```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return 'ValueError'
    return min(nums), max(nums)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
```
![](images/A/lab02/a1.png)

## A2
```
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![](images/A/lab02/a2.png)

## A3
```
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for element in mat:
        if isinstance(element, (list, tuple)):
            result.extend(element)
        else:
            return 'TypeError'
    return result

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![](images/A/lab02/a3.png)

## Задание В 
## B1
```
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            return 'ValueError'
    return [[mat[i][j] for i in range(len(mat))] for j in range(num_cols)]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
```
![](images/A/lab02/b1.png)

## B2
```
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            return 'ValueError'
    return [sum(row) for row in mat]

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```
![](images/A/lab02/b2.png)

## B3
```
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
           return 'ValueError'
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(num_cols)]

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![](images/A/lab02/b3.png)

## Задание С
## C1
```
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    parts = fio.split()
    surname = parts[0]
    initials = ''.join(f"{name[0].upper()}." for name in parts[1:])
    return f"{surname[0].upper()}{surname[1:]} {initials}, гр. {group}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![](images/A/lab02/c1.png)

## С2
```
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    fio_parts = ' '.join(fio.split()).split()
    if len(fio_parts) < 2:
        return "ValueError"
    initials = []
    for name in fio_parts[1:]:  
        if name: 
            initials.append(f"{name[0].upper()}.")
    surname = fio_parts[0].title()
    return f"{surname} {' '.join(initials)}, гр. {' '.join(group.split())}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```

![](images/A/lab02/c2.png)




# Лабораторная работа 1 

## Задание 1 
```
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![](images/lab01/01.png)

## Задание 2 
```

def f(number):
    return float(number.replace(',', '.'))
num1 = f(input("ввведите 1 число - "))
num2 = f(input("введите 2 число - "))

_sum = num1 + num2
avg = _sum / 2

print(f"sum={_sum:.2f}; avg={avg:.2f}")
```
![](images/lab01/02.png)

## Задание 3
```

price = float(input("цену -" ))
discount = float(input("сикдка -"))
vat = float(input("ндс -"))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"{base:.2f}")
print(f"{vat_amount:.2f}")
print(f"{total:.2f}")
```
![](images/lab01/03.png)

## Задание 4
 ```

 m = int(input("Введите кол-во минут:"))

hours = m // 60
minutes = m % 60

print(f"{hours:02d}:{minutes:02d}")
 ```
![](images/lab01/04.png)

 ## Задание 5 

```

fio = input().strip() # strip- удаляет лишние пробелы 
parts = fio.split()
initsial = ''.join(part[0].upper() for part in parts)
cleaned_length = len(' '.join(parts))
print(f"{initsial} {cleaned_length}")
```
![](images/lab01/05.png)

 ## Задание 6
 ```
N = int(input())
count_full_time = 0
count_part_time = 0

for _ in range(N):
    line = input().split()
    participation_format = line[3] == 'True'
    if participation_format:
        count_full_time += 1
    else:
        count_part_time += 1

print(count_full_time, count_part_time)
 ```
 ![](images/lab01/06.png)
