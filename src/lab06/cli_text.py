import argparse
from pathlib import Path
import sys

def cat_command(input_path: str, numbered: bool = False): # нумерация. булл имеет только два значеия t и F
    """Вывод содержимого файла построчно"""
    path = Path(input_path)
    if not path.exists():
        print(f"Ошибка: файл '{input_path}' не найден.", file=sys.stderr)
        sys.exit(1)

    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if numbered:
                print(f"{i:4d}: {line.rstrip()}") # rstrip() убирает символы перевода строки
            else:
                print(line.rstrip()) # удаляет пробельные символы справа


def stats_command(input_path: str, top_n: int = 5):
    """Простейший анализ частот слов (упрощённо, если нет lab03)"""
    path = Path(input_path)
    if not path.exists():
        print(f"Ошибка: файл '{input_path}' не найден.", file=sys.stderr)
        sys.exit(1)

    with path.open(encoding="utf-8") as f:
        text = f.read().lower() # читает как одну строку, переводит текст в нижний регистр 

    words = [w.strip(".,!?;:\"'()[]") for w in text.split()] # удаляет знаки препинания с начала и конца каждого слова
    freq = {} # словарь. для счета частот 
    for w in words:
        if not w:
            continue
        freq[w] = freq.get(w, 0) + 1 #  получает значение по ключу w, если нет - возвращает 0

    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]
    # возвращает пары, сортирует по второму элементу (частоте), по убыванию
    print(f"Топ {top_n} слов в '{input_path}':")
    for word, count in sorted_items:
        print(f"{word:15s} {count}")  #  форматирование: строка word занимает 15 символов


def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты для анализа текста (cat, stats)")# создает объект-парсер для обработки командной строки
    subparsers = parser.add_subparsers(dest="command", required=True)
    # переменная для управления подкомандами, добавляет возможность создавать подкоманды, куда сохранять имя выбранной команды (в args.command)
    # ---- cat ----
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу") #  аргумент ОБЯЗАТЕЛЕН для команды cat , инпут - имя аргумента 
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # ---- stats ----
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу") # при наличии флага устанавливает значение True
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")

    args = parser.parse_args()
    #Читает что ввел пользователь в командной строке, Проверяет правильность аргументов, Создает объект с удобным доступом к значениям

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
if __name__ == "__main__":
    main()

# if args.command == "cat": - проверяет, выбрал ли пользователь команду "cat"
# cat_command(args.input, args.n) - если ДА, вызывает функцию cat_command:

# args.input - путь к файлу из аргумента --input
# args.n - True/False из флага -n
# elif args.command == "stats": - иначе проверяет команду "stats"
# stats_command(args.input, args.top) - вызывает функцию stats_command:

# args.input - путь к файлу
# args.top - число из аргумента --top
