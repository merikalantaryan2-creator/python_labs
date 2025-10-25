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

