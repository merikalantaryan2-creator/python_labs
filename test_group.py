#!/usr/bin/env python3
"""
Тестирование класса Group для работы с CSV-хранилищем студентов
Лабораторная работа 9: База данных на CSV
"""

import os
import sys
from pathlib import Path

# Добавляем путь к src для импорта
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from src.lab09.group import Group, Student


def print_separator(title=""):
    """Печатает разделитель с заголовком"""
    if title:
        print(f"\n{'='*60}")
        print(f"{title.upper():^60}")
        print(f"{'='*60}")
    else:
        print("-" * 60)


def test_initialization():
    """Тест инициализации группы"""
    print_separator("1. Тест инициализации")
    
    # Тестовый файл
    test_file = "data/lab09/students.csv"
    
    print(f"Создание группы с файлом: {test_file}")
    
    # Убедимся, что директория существует
    os.makedirs(Path(test_file).parent, exist_ok=True)
    
    # Удаляем старый файл для чистого теста
    if os.path.exists(test_file):
        os.remove(test_file)
        print("Старый файл удален")
    
    # Создаем группу
    group = Group(test_file)
    print(f"Группа создана")
    print(f"Файл существует: {os.path.exists(test_file)}")
    
    # Проверяем содержимое файла
    with open(test_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
        print(f"Содержимое файла:\n{content}")
    
    return group, test_file


def test_add_students(group):
    """Тест добавления студентов"""
    print_separator("2. Тест добавления студентов")
    
    # Создаем тестовых студентов - ВНИМАНИЕ: третий параметр это ВОЗРАСТ (int), а не группа!
    students = [
        Student("Иванов Иван Иванович", "БИВТ-21-1", 20, 4.3),  # Возраст: 20
        Student("Петров Петр Петрович", "БИВТ-21-1", 21, 4.7),  # Возраст: 21
        Student("Сидорова Анна Сергеевна", "БИВТ-21-2", 20, 4.9),  # Возраст: 20
        Student("Кузнецов Алексей Викторович", "БИВТ-21-1", 22, 3.8),  # Возраст: 22
        Student("Смирнова Мария Дмитриевна", "БИВТ-21-3", 19, 4.5),  # Возраст: 19
    ]
    
    print("Добавляем студентов:")
    for i, student in enumerate(students, 1):
        group.add(student)
        print(f"{i}. {student.fio} - {student.group} (возраст: {student.age}, GPA: {student.gpa})")
    
    # Пробуем добавить дубликат (должна быть ошибка)
    print("\nПопытка добавить дубликат:")
    try:
        group.add(students[0])
        print("ОШИБКА: Дубликат добавлен (не должно быть)")
    except ValueError as e:
        print(f"✓ Ошибка поймана как и ожидалось: {e}")
    
    return students


def test_list_students(group):
    """Тест получения списка студентов"""
    print_separator("3. Тест получения списка студентов")
    
    students = group.list()
    print(f"Всего студентов: {len(students)}\n")
    
    print("{:<30} {:<15} {:<6} {:<5}".format(
        "ФИО", "Группа", "Возраст", "GPA"
    ))
    print("-" * 60)
    
    for student in students:
        print("{:<30} {:<15} {:<6} {:<5.2f}".format(
            student.fio[:30],
            student.group,
            student.age,
            student.gpa
        ))


def test_find_students(group):
    """Тест поиска студентов"""
    print_separator("4. Тест поиска студентов")
    
    # Поиск по разным подстрокам
    search_queries = ["иванов", "петр", "анна", "алексей", "мария"]
    
    for query in search_queries:
        print(f"\nПоиск по запросу '{query}':")
        found = group.find(query)
        
        if found:
            for student in found:
                print(f"  ✓ {student.fio} ({student.group}, возраст: {student.age}, GPA: {student.gpa})")
        else:
            print(f"  ✗ Ничего не найдено")
    
    # Поиск по части фамилии
    print(f"\nПоиск по части фамилии 'ов':")
    found = group.find("ов")
    print(f"Найдено студентов: {len(found)}")
    for student in found:
        print(f"  {student.fio} (возраст: {student.age})")


def test_update_student(group):
    """Тест обновления студента"""
    print_separator("5. Тест обновления студента")
    
    # Обновляем Петрова
    target_fio = "Петров Петр Петрович"
    print(f"Обновляем студента: {target_fio}")
    
    # Проверяем текущие данные
    current = group.find("Петров")[0]
    print(f"Текущие данные: {current.group}, возраст: {current.age}, GPA: {current.gpa}")
    
    # Обновляем - ВНИМАНИЕ: age должен быть int, gpa - float
    success = group.update(
        target_fio,
        group="БИВТ-21-2",    # строка
        age=22,               # целое число
        gpa=4.8               # дробное число
    )
    
    if success:
        print("✓ Студент обновлен")
        
        # Проверяем обновленные данные
        updated = group.find("Петров")[0]
        print(f"Обновленные данные: {updated.group}, возраст: {updated.age}, GPA: {updated.gpa}")
    else:
        print("✗ Студент не найден")
    
    # Пробуем обновить несуществующего студента
    print("\nПопытка обновить несуществующего студента:")
    success = group.update("Несуществующий Студент", gpa=5.0)
    if not success:
        print("✓ Как и ожидалось, студент не найден")


def test_remove_student(group):
    """Тест удаления студента"""
    print_separator("6. Тест удаления студента")
    
    # Удаляем Кузнецова
    target_fio = "Кузнецов Алексей Викторович"
    print(f"Удаляем студента: {target_fio}")
    
    # Проверяем, существует ли перед удалением
    exists_before = len(group.find("Кузнецов")) > 0
    print(f"Студент существует перед удалением: {exists_before}")
    
    # Удаляем
    removed = group.remove(target_fio)
    print(f"Результат удаления: {removed}")
    
    # Проверяем, что удален
    exists_after = len(group.find("Кузнецов")) > 0
    print(f"Студент существует после удаления: {exists_after}")
    
    # Пробуем удалить еще раз
    print("\nПопытка удалить уже удаленного студента:")
    removed_again = group.remove(target_fio)
    print(f"Результат: {removed_again} (False - как и ожидалось)")
    
    return exists_before and not exists_after and removed


def test_statistics(group):
    """Тест статистики (дополнительное задание)"""
    print_separator("7. Тест статистики")
    
    stats = group.stats()
    
    print(f"📊 Статистика по группе:")
    print(f"   Всего студентов: {stats['count']}")
    print(f"   Средний GPA: {stats['avg_gpa']:.2f}")
    
    print(f"\n   Распределение по группам:")
    for group_name, count in stats['groups'].items():
        print(f"     {group_name}: {count} студентов")
    
    # Дополнительно покажем средний возраст
    students = group.list()
    if students:
        avg_age = sum(student.age for student in students) / len(students)
        print(f"\n   Средний возраст: {avg_age:.1f} лет")


def test_empty_group():
    """Тест работы с пустой группой"""
    print_separator("8. Тест пустой группы")
    
    # Создаем новую пустую группу
    empty_file = "data/lab09/empty_group.csv"
    if os.path.exists(empty_file):
        os.remove(empty_file)
    
    empty_group = Group(empty_file)
    
    # Проверяем методы
    print("Тестируем методы для пустой группы:")
    print(f"  Список студентов: {len(empty_group.list())}")
    print(f"  Поиск 'Иванов': {len(empty_group.find('Иванов'))}")
    print(f"  Удаление 'Иванов': {empty_group.remove('Иванов')}")
    print(f"  Обновление 'Иванов': {empty_group.update('Иванов', age=20, gpa=5.0)}")
    
    # Статистика пустой группы
    empty_stats = empty_group.stats()
    print(f"  Статистика: {empty_stats['count']} студентов")
    
    # Очищаем
    os.remove(empty_file)


def test_csv_content(filepath):
    """Показывает содержимое CSV файла"""
    print_separator("9. Содержимое CSV файла")
    
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            print(f"Файл: {filepath}")
            print(f"Количество строк: {len(lines)}\n")
            
            # Красиво выводим таблицу
            for i, line in enumerate(lines, 1):
                if i == 1:  # заголовок
                    print("Заголовок:", line.strip())
                    print("-" * 50)
                else:
                    parts = line.strip().split(',')
                    if len(parts) >= 4:
                        print(f"{i-1:2}. {parts[0]:30} {parts[1]:15} {parts[2]:>6} {parts[3]:>5}")
    else:
        print(f"Файл не найден: {filepath}")


def main():
    """Основная функция тестирования"""
    print("="*60)
    print("ЛАБОРАТОРНАЯ РАБОТА 9: БАЗА ДАННЫХ НА CSV".center(60))
    print("Тестирование класса Group с CRUD-операциями".center(60))
    print("="*60)
    
    try:
        # 1. Инициализация
        group, test_file = test_initialization()
        
        # 2. Добавление
        students = test_add_students(group)
        
        # 3. Вывод списка
        test_list_students(group)
        
        # 4. Поиск
        test_find_students(group)
        
        # 5. Обновление
        test_update_student(group)
        
        # 6. Удаление
        test_remove_student(group)
        
        # 7. Статистика
        test_statistics(group)
        
        # 8. Показываем финальное содержимое CSV
        test_csv_content(test_file)
        
        # 9. Тест пустой группы
        test_empty_group()
        
        print_separator("ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
        print("✓ Все тесты выполнены успешно!")
        print(f"\nИтоговый файл: {test_file}")
        print(f"Количество студентов в базе: {len(group.list())}")
        
    except Exception as e:
        print(f"\n✗ Ошибка во время тестирования: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())