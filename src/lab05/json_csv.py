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

    if json_file.suffix.lower() != ".json":
        raise ValueError(
            f"Неверный тип файла: ожидается .json, получен {json_file.suffix}"
        )

    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)  # загрузка JSON данных
    except json.JSONDecodeError as e:
        raise ValueError(f"Ошибка декодирования JSON: {e}")

    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список объектов")

    if not data:
        raise ValueError("JSON файл пустой")

    if not all(isinstance(item, dict) for item in data):
        raise ValueError("Все элементы JSON должны быть словарями")

    all_fields = set()  # создает множество для уникальных полей
    for item in data:
        all_fields.update(item.keys())  # добавляет ключи каждого словаря
    fieldnames = sorted(all_fields)

    try:
        with open(csv_file, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for row in data:
                complete_row = {field: str(row.get(field, "")) for field in fieldnames}
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

    if csv_file.suffix.lower() != ".csv":
        raise ValueError(
            f"Неверный тип файла: ожидается .csv, получен {csv_file.suffix}"
        )

    try:
        with open(csv_file, "r", encoding="utf-8") as f:
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
        string_row = {
            key: str(value) if value is not None else "" for key, value in row.items()
        }
        data.append(string_row)

    try:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    except Exception as e:
        raise ValueError(f"Ошибка записи JSON: {e}")

    # пример использования


if __name__ == "__main__":
    # JSON -> CSV
    json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")

    # CSV -> JSON
    csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
