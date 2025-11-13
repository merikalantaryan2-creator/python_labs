
"""
CLI-утилиты для анализа текста (cat, stats)
ЛР6 — argparse
"""

import argparse
from pathlib import Path
import sys

# Импортируем функции из предыдущих лабораторных
# from src.lab03.text_stats import word_frequencies  # пример
# from src.lib.io_helpers import read_text_file      # пример


def cat_command(input_path: str, numbered: bool = False):
    """Вывод содержимого файла построчно"""
    path = Path(input_path)
    if not path.exists():
        print(f"Ошибка: файл '{input_path}' не найден.", file=sys.stderr)
        sys.exit(1)

    with path.open(encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if numbered:
                print(f"{i:4d}: {line.rstrip()}")
            else:
                print(line.rstrip())


def stats_command(input_path: str, top_n: int = 5):
    """Простейший анализ частот слов (упрощённо, если нет lab03)"""
    path = Path(input_path)
    if not path.exists():
        print(f"Ошибка: файл '{input_path}' не найден.", file=sys.stderr)
        sys.exit(1)

    with path.open(encoding="utf-8") as f:
        text = f.read().lower()

    words = [w.strip(".,!?;:\"'()[]") for w in text.split()]
    freq = {}
    for w in words:
        if not w:
            continue
        freq[w] = freq.get(w, 0) + 1

    sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:top_n]

    print(f"Топ {top_n} слов в '{input_path}':")
    for word, count in sorted_items:
        print(f"{word:15s} {count}")


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты для анализа текста (cat, stats)"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # ---- cat ----
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # ---- stats ----
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество топ-слов")

    args = parser.parse_args()

    if args.command == "cat":
        cat_command(args.input, args.n)
    elif args.command == "stats":
        stats_command(args.input, args.top)
if __name__ == "__main__":
    main()
