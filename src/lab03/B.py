
# Нормализуем и токенизируем текст
normalized_text = normalize(text)
tokens = tokenize(normalized_text)

# Подсчитываем статистику
freq = count_freq(tokens)
total_words = len(tokens)
unique_words = len(freq)
top_words = top_n(freq, 5)

print(f"Всего слов: {total_words}")
print(f"Уникальных слов: {unique_words}")
print("Топ-5:")
for word, count in top_words:
    print(f"{word}:{count}")