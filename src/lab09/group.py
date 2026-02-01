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