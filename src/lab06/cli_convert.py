
"""
CLI-конвертер форматов данных (json2csv, csv2json, csv2xlsx)
ЛР6 — argparse
"""

import argparse
from pathlib import Path
import sys

# from src.lab05.json_csv import json_to_csv, csv_to_json
# from src.lab05.csv_xlsx import csv_to_xlsx


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