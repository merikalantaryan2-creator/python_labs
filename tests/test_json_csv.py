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
