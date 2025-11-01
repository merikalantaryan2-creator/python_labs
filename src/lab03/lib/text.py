import re 

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

