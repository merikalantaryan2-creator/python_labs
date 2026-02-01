import re
import argparse
from pathlib import Path
from io_txt_csv import read_text, write_csv


def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text = text.replace("\n", " ").replace("\t", " ").replace("\r", " ")
    while "  " in text:
        text = text.replace("  ", " ")
    text = text.strip()
    if yo2e:
        text = text.replace("ё", "е").replace("Ё", "Е")
    if casefold:
        text = text.casefold()
    return text


def tokenize(text: str) -> list[str]:
    text = "".join(
        char
        for char in text
        if char.isalpha() or char.isspace() or char == "-" or char in "0123456789"
    )
    text = text.split()
    return text


def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(
        freq.items(), key=lambda x: (-x[1], x[0])
    )  # получаем пары слов,сорт(по уб,по вз)
    return sorted_items[:n]


def main():
    parser = argparse.ArgumentParser(description="Анализ текста и создание отчета")
    parser.add_argument(
        "--in",
        dest="input_file",
        default="data/lab04/input.txt",
        help="Входной текстовый файл (по умолчанию: data/lab04/input.txt)",
    )
    parser.add_argument(
        "--out",
        dest="output_file",
        default="data/lab04/report.csv",
        help="Выходной CSV файл (по умолчанию: data/lab04/report.csv)",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="Кодировка файла (по умолчанию: utf-8, для Windows: cp1251)",
    )
    args = parser.parse_args()

    try:
        print(f"Чтение файла: {args.input_file}")
        text = read_text(args.input_file, encoding=args.encoding)
        print("Анализ текста...")
        normalized = normalize(text)
        tokens = tokenize(normalized)
        word_counts = count_freq(tokens)
        sorted_words = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
        print(f"Сохранение отчета: {args.output_file}")
        rows = [(word, count) for word, count in sorted_words]
        header = ("word", "count")
        write_csv(rows, args.output_file, header)
        print("\n--- ОТЧЕТ ---")
        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(word_counts)}")
        print("Топ-5:")
        freq = count_freq(tokens)
        top_words = top_n(freq, 5)
        for word, count in top_words:
            print(f"{word}:{count}")
        print(f"\nОтчет сохранен в: {args.output_file}")

    except FileNotFoundError:
        return "FileNotFoundError"
    except UnicodeDecodeError:
        return "UnicodeDecodeError"
    except Exception:
        return "Exception"


if __name__ == "__main__":
    main()
