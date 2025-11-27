def tokenize(text: str) -> list[str]:
    text = "".join(
        char
        for char in text
        if char.isalpha() or char.isspace() or char == "-" or char in "0123456789"
    )
    text = text.split()
    return text


print(tokenize("привет мир"))
print(tokenize("hello, world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
