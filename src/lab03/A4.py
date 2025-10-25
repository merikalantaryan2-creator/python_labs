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
