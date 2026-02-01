import sys  # Импорт модуля для работы с системными параметрами
import os   # Импорт модуля для работы с операционной системой

# Добавление родительской директории в путь для импорта модулей проекта
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest  # Импорт фреймворка для тестирования
import json    # Импорт модуля для работы с JSON
import csv     # Импорт модуля для работы с CSV
from pathlib import Path  # Импорт для работы с путями файловой системы
from src.lab05.json_csv import json_to_csv, csv_to_json  # Импорт тестируемых функций


class TestJsonToCsv:
    """Тесты для функции json_to_csv"""

    def test_json_to_csv_basic(self, tmp_path: Path):
        """Тест базовой конвертации JSON в CSV"""
        src = tmp_path / "test.json"  # Создание пути для исходного JSON файла
        dst = tmp_path / "test.csv"   # Создание пути для целевого CSV файла

        data = [  # Тестовые данные в формате списка словарей
            {"name": "Alice", "age": 25, "city": "Moscow"},
            {"name": "Bob", "age": 30, "city": "SPb"},
            {"name": "Charlie", "age": 35, "city": "Kazan"},
        ]

        # Запись тестовых данных в JSON файл
        src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        # Вызов тестируемой функции для конвертации
        json_to_csv(str(src), str(dst))

        # Проверяем, что файл создан
        assert dst.exists()

        # Проверяем содержимое CSV
        with dst.open(encoding="utf-8") as f:  # Открываем CSV файл для чтения
            reader = csv.DictReader(f)  # Создаем DictReader для чтения CSV как словарей
            rows = list(reader)  # Преобразуем reader в список строк

        assert len(rows) == 3  # Проверяем количество строк
        assert set(rows[0].keys()) == {"name", "age", "city"}  # Проверяем заголовки столбцов
        assert rows[0]["name"] == "Alice"  # Проверяем значение в первом столбце
        assert rows[0]["age"] == "25"      # Проверяем значение во втором столбце (число преобразовано в строку)

    def test_json_to_csv_different_keys(self, tmp_path: Path):
        """Тест с объектами, имеющими разные ключи"""
        src = tmp_path / "test.json"  # Путь к исходному JSON файлу
        dst = tmp_path / "test.csv"   # Путь к целевому CSV файлу

        data = [  # Данные с разными наборами ключей в каждом объекте
            {"name": "Alice", "age": 25},
            {"name": "Bob", "city": "SPb"},  # Нет age
            {"name": "Charlie", "age": 35, "country": "Russia"},  # Дополнительный ключ
        ]

        # Запись данных в JSON файл
        src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        # Конвертация JSON в CSV
        json_to_csv(str(src), str(dst))

        with dst.open(encoding="utf-8") as f:  # Чтение результата
            reader = csv.DictReader(f)
            rows = list(reader)

        assert len(rows) == 3  # Проверяем количество строк
        # Все возможные ключи должны быть в заголовках
        assert set(rows[0].keys()) == {"name", "age", "city", "country"}

    def test_json_to_csv_file_not_found(self):
        """Тест на несуществующий файл"""
        with pytest.raises(FileNotFoundError):  # Ожидаем исключение FileNotFoundError
            json_to_csv("nonexistent.json", "output.csv")  # Попытка конвертации несуществующего файла

    def test_json_to_csv_invalid_json(self, tmp_path: Path):
        """Тест на некорректный JSON"""
        src = tmp_path / "invalid.json"  # Путь к файлу с некорректным JSON
        dst = tmp_path / "test.csv"      # Путь к целевому файлу

        src.write_text("{ invalid json }", encoding="utf-8")  # Запись некорректного JSON

        with pytest.raises(ValueError):  # Ожидаем исключение ValueError
            json_to_csv(str(src), str(dst))  # Попытка конвертации некорректного JSON

    def test_json_to_csv_empty_json(self, tmp_path: Path):
        """Тест на пустой JSON - должен вызывать ошибку"""
        src = tmp_path / "empty.json"  # Путь к файлу с пустым JSON
        dst = tmp_path / "test.csv"    # Путь к целевому файлу

        src.write_text("[]", encoding="utf-8")  # Запись пустого массива JSON

        # Ожидаем ValueError для пустого JSON
        with pytest.raises(ValueError, match="JSON файл пустой"):
            json_to_csv(str(src), str(dst))

        # Убеждаемся, что CSV файл не создан
        assert not dst.exists()


class TestCsvToJson:
    """Тесты для функции csv_to_json"""

    def test_csv_to_json_basic(self, tmp_path: Path):
        """Тест базовой конвертации CSV в JSON"""
        src = tmp_path / "test.csv"   # Путь к исходному CSV файлу
        dst = tmp_path / "test.json"  # Путь к целевому JSON файлу

        csv_content = """name,age,city
Alice,25,Moscow
Bob,30,SPb
Charlie,35,Kazan"""  # CSV данные с заголовком и тремя строками

        src.write_text(csv_content, encoding="utf-8")  # Запись CSV данных в файл
        csv_to_json(str(src), str(dst))  # Конвертация CSV в JSON

        # Проверяем, что файл создан
        assert dst.exists()

        # Проверяем содержимое JSON
        with dst.open(encoding="utf-8") as f:  # Открываем JSON файл для чтения
            data = json.load(f)  # Загружаем JSON данные

        assert len(data) == 3  # Проверяем количество объектов
        assert data[0] == {"name": "Alice", "age": "25", "city": "Moscow"}  # Проверяем первый объект
        assert data[1] == {"name": "Bob", "age": "30", "city": "SPb"}       # Проверяем второй объект

    def test_csv_to_json_empty_values(self, tmp_path: Path):
        """Тест с пустыми значениями в CSV"""
        src = tmp_path / "test.csv"   # Путь к исходному CSV файлу
        dst = tmp_path / "test.json"  # Путь к целевому JSON файлу

        csv_content = """name,age,city
Alice,25,Moscow
Bob,,SPb
Charlie,35,"""  # CSV с пустыми значениями

        src.write_text(csv_content, encoding="utf-8")  # Запись CSV в файл
        csv_to_json(str(src), str(dst))  # Конвертация

        with dst.open(encoding="utf-8") as f:  # Чтение результата
            data = json.load(f)

        assert data[1] == {"name": "Bob", "age": "", "city": "SPb"}    # Проверка строки с пустым age
        assert data[2] == {"name": "Charlie", "age": "35", "city": ""} # Проверка строки с пустым city

    def test_csv_to_json_file_not_found(self):
        """Тест на несуществующий файл"""
        with pytest.raises(FileNotFoundError):  # Ожидаем исключение
            csv_to_json("nonexistent.csv", "output.json")  # Попытка конвертации несуществующего файла

    def test_csv_to_json_empty_csv(self, tmp_path: Path):
        """Тест на пустой CSV"""
        src = tmp_path / "empty.csv"  # Путь к пустому CSV файлу
        dst = tmp_path / "test.json"  # Путь к целевому JSON файлу

        src.write_text("", encoding="utf-8")  # Создание пустого файла

        with pytest.raises(ValueError):  # Ожидаем исключение
            csv_to_json(str(src), str(dst))  # Попытка конвертации пустого CSV


class TestRoundTrip:
    """Тесты на полный цикл конвертации"""

    def test_json_csv_json_roundtrip(self, tmp_path: Path):
        """Тест полного цикла JSON -> CSV -> JSON"""
        original_json = tmp_path / "original.json"        # Исходный JSON файл
        intermediate_csv = tmp_path / "intermediate.csv"  # Промежуточный CSV файл
        final_json = tmp_path / "final.json"              # Финальный JSON файл

        original_data = [  # Исходные тестовые данные
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
        assert len(final_data) == len(original_data)  # Проверяем количество записей
        assert final_data[0]["name"] == original_data[0]["name"]  # Имя должно совпадать
        assert final_data[0]["age"] == str(original_data[0]["age"])  # Число -> строка
        assert final_data[0]["city"] == original_data[0]["city"]     # Город должен совпадать