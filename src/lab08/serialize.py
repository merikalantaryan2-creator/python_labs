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