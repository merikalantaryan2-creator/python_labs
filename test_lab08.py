#!/usr/bin/env python3
"""Тестирование функционала лабораторной работы 8."""

import sys
import os
from pathlib import Path

# Добавляем путь к src в sys.path
current_dir = Path(__file__).parent
src_dir = current_dir / 'src'
sys.path.insert(0, str(src_dir))

from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json


def main():
    """Основная функция тестирования."""
    
    # 1. Создаем студентов
    print("=" * 50)
    print("Создание студентов:")
    print("=" * 50)
    
    student1 = Student(
        fio="Иванов Иван Иванович",
        birthdate="2000-05-15",
        group="SE-01",
        gpa=4.5
    )
    
    student2 = Student(
        fio="Петрова Анна Сергеевна",
        birthdate="2001-11-23",
        group="CS-02",
        gpa=4.8
    )
    
    # Проверяем методы
    print(f"Студент 1: {student1.fio}")
    print(f"Возраст: {student1.age()} лет")
    print(f"Словарь: {student1.to_dict()}")
    print()
    print(student1)
    print()
    
    # 2. Тестирование валидации
    print("=" * 50)
    print("Тестирование валидации:")
    print("=" * 50)
    
    try:
        # Неверный формат даты
        Student("Тест", "2000/05/15", "GR-01", 4.0)
    except ValueError as e:
        print(f"Ожидаемая ошибка: {e}")
    
    try:
        # Неверный диапазон GPA
        Student("Тест", "2000-05-15", "GR-01", 6.0)
    except ValueError as e:
        print(f"Ожидаемая ошибка: {e}")
    
    # 3. Сериализация и десериализация
    print("=" * 50)
    print("Сериализация и десериализация:")
    print("=" * 50)
    
    students = [student1, student2]
    
    # Сохраняем в JSON
    output_path = "data/lab08/students_output.json"
    students_to_json(students, output_path)
    print(f"Студенты сохранены в {output_path}")
    
    # Загружаем из JSON
    input_path = "data/lab08/students_input.json"
    loaded_students = students_from_json(input_path)
    
    print(f"\nЗагружено студентов: {len(loaded_students)}")
    for i, student in enumerate(loaded_students, 1):
        print(f"\nСтудент {i}:")
        print(student)
    
    # 4. Тестирование from_dict
    print("=" * 50)
    print("Тестирование from_dict:")
    print("=" * 50)
    
    student_dict = {
        "fio": "Новый Студент",
        "birthdate": "2002-02-28",
        "group": "TEST-01",
        "gpa": 3.7
    }
    
    new_student = Student.from_dict(student_dict)
    print(f"Создан из словаря: {new_student}")
    print(f"Тип: {type(new_student)}")
    print(f"Возраст: {new_student.age()}")


if __name__ == "__main__":
    main()