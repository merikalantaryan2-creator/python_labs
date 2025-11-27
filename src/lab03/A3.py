def count_freq(tokens: list[str]) -> dict[str, int]:
    freq = {}
    for token in tokens:
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1
    return freq


tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = count_freq(tokens2)

print(f"Токены {tokens1} → частоты {freq1}")
print(f"Токены {tokens2} → частоты {freq2}")
