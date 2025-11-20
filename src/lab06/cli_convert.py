import argparse # для обработки аргументов командной строки
from pathlib import Path 
import sys


def check_file_exists(path_str: str):
    path = Path(path_str)
    if not path.exists(): # проверяет  существует ли файл 
        print(f"Ошибка: входной файл '{path}' не найден.", file=sys.stderr)
        sys.exit(1) # завершает программу с кодом ошибки 1 
    return path

def json2csv(input_path: str, output_path: str):
    check_file_exists(input_path) #  проверяет что входной файл существует

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
    parser = argparse.ArgumentParser(description="CLI-конвертеры данных (ЛР6)") # создает парсер аргументов
    sub = parser.add_subparsers(dest="cmd", required=True) # создает подпарсеры для подкоманд
    
    #Парсер — это программа или скрипт, который автоматически извлекает, анализирует и структурирует данные из различных источников, таких как веб-страницы, файлы или базы данных

    # ---- json2csv ----
    p1 = sub.add_parser("json2csv", help="Преобразовать JSON в CSV") # создает парсер для подкоманды
    p1.add_argument("--in", dest="input", required=True, help="Входной JSON-файл") 
    p1.add_argument("--out", dest="output", required=True, help="Выходной CSV-файл")
    # dest="input" - куда сохранить значение (в args.input)
    # ---- csv2json ----
    p2 = sub.add_parser("csv2json", help="Преобразовать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p2.add_argument("--out", dest="output", required=True, help="Выходной JSON-файл")

    # ---- csv2xlsx ----
    p3 = sub.add_parser("csv2xlsx", help="Преобразовать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True, help="Входной CSV-файл")
    p3.add_argument("--out", dest="output", required=True, help="Выходной XLSX-файл")

    args = parser.parse_args() # объясни args = parser.parse_args()
    # анализ командной строки

    if args.cmd == "json2csv": # это атрибут объекта args, который содержит название выбранной подкоманды.
        json2csv(args.input, args.output)
    elif args.cmd == "csv2json":
        csv2json(args.input, args.output)
    elif args.cmd == "csv2xlsx":
        csv2xlsx(args.input, args.output)
if __name__ == "__main__":
    main()