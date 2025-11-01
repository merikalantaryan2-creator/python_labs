# Калантарян Мери 

# Лабараторная работа 4 

## io_txt_csv
```
import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    with open(path, 'r', encoding=encoding) as file:
        return file.read()

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if rows:
        first_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len:
                raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидается {first_len}")
    ensure_parent_dir(path)
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        if header is not None:
            writer.writerow(header)
        writer.writerows(rows)

def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
```
## text_report
```
import re
import argparse
from pathlib import Path
from io_txt_csv import read_text, write_csv

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=text.replace('\n',' ').replace('\t',' ').replace('\r',' ')
    while '  ' in text:
        text=text.replace('  ',' ')
    text=text.strip()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    if casefold:
        text=text.casefold()
    return text



def tokenize(text: str) -> list[str]:
    text=''.join(char for char in text if char.isalpha()\
    or char.isspace() or char == '-' or char in '0123456789')
    text=text.split()
    return text

def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] =1
    return freq


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))#получаем пары слов,сорт(по уб,по вз)
    return sorted_items[:n]



def main():
    parser = argparse.ArgumentParser(description='Анализ текста и создание отчета')
    parser.add_argument('--in', dest='input_file', default='data/lab04/input.txt',
                       help='Входной текстовый файл (по умолчанию: data/lab04/input.txt)')
    parser.add_argument('--out', dest='output_file', default='data/lab04/report.csv',
                       help='Выходной CSV файл (по умолчанию: data/lab04/report.csv)')
    parser.add_argument('--encoding', default='utf-8',
                       help='Кодировка файла (по умолчанию: utf-8, для Windows: cp1251)')
    args = parser.parse_args()
    
    try:
        print(f"Чтение файла: {args.input_file}")
        text = read_text(args.input_file, encoding=args.encoding)
        print("Анализ текста...")
        normalized = normalize(text)
        tokens = tokenize(normalized)
        word_counts = count_freq(tokens)
        sorted_words = sorted(word_counts.items(), 
                             key=lambda x: (-x[1], x[0]))
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
        return 'FileNotFoundError'
    except UnicodeDecodeError:
        return 'UnicodeDecodeError'
    except Exception:
        return 'Exception'

if __name__ == "__main__":
    main()
```


# Лабараторная работа 3

## Задание А 
## А1
```
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    text=text.replace('\n',' ').replace('\t',' ').replace('\r',' ')
    while '  ' in text:
        text=text.replace('  ',' ')
    text=text.strip()
    if yo2e:
        text=text.replace('ё','е').replace('Ё','Е')
    if casefold:
        text=text.casefold()
    return text

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```
![](images/A/lab03/A1.png)

## A2
```
def tokenize(text: str) -> list[str]:
    text=''.join(char for char in text if char.isalpha()\
    or char.isspace() or char == '-' or char in '0123456789')
    text=text.split()
    return text
print(tokenize("привет мир"))
print(tokenize("hello, world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
![](images/A/lab03/A2.png)

## A3
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] =1
    return freq

tokens1 = ["a","b","a","c","b","a"]
freq1 = count_freq(tokens1)
tokens2 = ["bb","aa","bb","aa","cc"]
freq2 = count_freq(tokens2)

print(f"Токены {tokens1} → частоты {freq1}")
print(f"Токены {tokens2} → частоты {freq2}")
```
![](images/A/lab03/A3.png)

## A4
```
def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] =1
    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))#получаем пары слов,сорт(по уб,по вз)
    return sorted_items[:n]

tokens1 = ["a","b","a","c","b","a"]
freq1 = count_freq(tokens1)
tokens2 = ["bb","aa","bb","aa","cc"]
freq2 = count_freq(tokens2)

print(f"top_n(..., n=2) → {top_n(freq1, 2)}")
print(f"top_n(..., n=2) → {top_n(freq2, 2)}")
```
![](images/A/lab03/A4.png)

## Задание В
```
import sys
import os
from lib import text as txt

def main():
    text = input()
    normalized_text = txt.normalize(text, casefold=True, yo2e=True)
    tokens = txt.tokenize(normalized_text)
    total_words = len(tokens)
    unique_words = len(set(tokens))
    freq = txt.count_freq(tokens)
    top_words = txt.top_n(freq, 5)
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    for word, count in top_words:
        print(f"{word}:{count}")
    ```
    ![](images/A/lab03/B.png)

# Лабараторная работа 2 

## Задание A
## A1
```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if not nums:
        return 'ValueError'
    return min(nums), max(nums)
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
```
![](images/A/lab02/a1.png)

## A2
```
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    return sorted(set(nums))

print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```
![](images/A/lab02/a2.png)

## A3
```
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for element in mat:
        if isinstance(element, (list, tuple)):
            result.extend(element)
        else:
            return 'TypeError'
    return result

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```
![](images/A/lab02/a3.png)

## Задание В 
## B1
```
def transpose(mat: list[list[float | int]]) -> list[list]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            return 'ValueError'
    return [[mat[i][j] for i in range(len(mat))] for j in range(num_cols)]

print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
```
![](images/A/lab02/b1.png)

## B2
```
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
            return 'ValueError'
    return [sum(row) for row in mat]

print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
```
![](images/A/lab02/b2.png)

## B3
```
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    num_cols = len(mat[0])
    for row in mat:
        if len(row) != num_cols:
           return 'ValueError'
    return [sum(mat[i][j] for i in range(len(mat))) for j in range(num_cols)]

print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```
![](images/A/lab02/b3.png)

## Задание С
## C1
```
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    parts = fio.split()
    surname = parts[0]
    initials = ''.join(f"{name[0].upper()}." for name in parts[1:])
    return f"{surname[0].upper()}{surname[1:]} {initials}, гр. {group}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![](images/A/lab02/c1.png)

## С2
```
def format_record(rec: tuple[str, str, float]) -> str:
    fio, group, gpa = rec
    fio_parts = ' '.join(fio.split()).split()
    if len(fio_parts) < 2:
        return "ValueError"
    initials = []
    for name in fio_parts[1:]:  
        if name: 
            initials.append(f"{name[0].upper()}.")
    surname = fio_parts[0].title()
    return f"{surname} {' '.join(initials)}, гр. {' '.join(group.split())}, GPA {gpa:.2f}"

print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![](images/A/lab02/c2.png)



# Лабораторная работа 1 

## Задание 1 **
```
name = input("Имя: ")
age = int(input("Возраст: "))
print(f"Привет, {name}! Через год тебе будет {age + 1}.")
```
![](images/lab01/01.png)

## Задание 2 
```

def f(number):
    return float(number.replace(',', '.'))
num1 = f(input("ввведите 1 число - "))
num2 = f(input("введите 2 число - "))

_sum = num1 + num2
avg = _sum / 2

print(f"sum={_sum:.2f}; avg={avg:.2f}")
```
![](images/lab01/02.png)

## Задание 3
```

price = float(input("цену -" ))
discount = float(input("сикдка -"))
vat = float(input("ндс -"))

base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount

print(f"{base:.2f}")
print(f"{vat_amount:.2f}")
print(f"{total:.2f}")
```
![](images/lab01/03.png)

## Задание 4
 ```

 m = int(input("Введите кол-во минут:"))

hours = m // 60
minutes = m % 60

print(f"{hours:02d}:{minutes:02d}")
 ```
![](images/lab01/04.png)

 ## Задание 5 
```

fio = input().strip() # strip- удаляет лишние пробелы 
parts = fio.split()
initsial = ''.join(part[0].upper() for part in parts)
cleaned_length = len(' '.join(parts))
print(f"{initsial} {cleaned_length}")
```
![](images/lab01/05.png)

 ## Задание 6
 ```
N = int(input())
count_full_time = 0
count_part_time = 0

for _ in range(N):
    line = input().split()
    participation_format = line[3] == 'True'
    if participation_format:
        count_full_time += 1
    else:
        count_part_time += 1

print(count_full_time, count_part_time)
 ```
 ![](images/lab01/06.png)
