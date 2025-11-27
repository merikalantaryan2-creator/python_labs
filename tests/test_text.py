import pytest
from src.lib.text import normalize, tokenize, count_freq, top_n


class TestNormalize:
    """Тесты для функции normalize"""

    @pytest.mark.parametrize(
        "source, expected",
        [
            ("ПрИвЕт\nМИр\t", "привет мир"),
            ("ёжик, Ёлка", "ежик, елка"),
            ("Hello\r\nWorld", "hello world"),
            ("  двойные   пробелы  ", "двойные пробелы"),
            ("", ""),
            ("   ", ""),
            ("ТЕСТ!!!", "тест!!!"),
            ("Много\t\t\tтабов", "много табов"),
        ],
    )
    def test_normalize_basic(self, source, expected):
        assert normalize(source) == expected


class TestTokenize:
    """Тесты для функции tokenize"""

    @pytest.mark.parametrize(
        "source, expected",
        [
            ("привет мир", ["привет", "мир"]),
            ("hello world test", ["hello", "world", "test"]),
            ("один, два. три!", ["один", "два", "три"]),
            ("", []),
            ("   ", []),
            ("только-только", ["только-только"]),
            ("раз     много     пробелов", ["раз", "много", "пробелов"]),
        ],
    )
    def test_tokenize_basic(self, source, expected):
        assert tokenize(source) == expected


class TestCountFreq:
    """Тесты для функции count_freq"""

    def test_count_freq_basic(self):
        tokens = ["я", "люблю", "python", "я", "python", "python"]
        result = count_freq(tokens)
        expected = {"я": 2, "люблю": 1, "python": 3}
        assert result == expected

    def test_count_freq_empty(self):
        assert count_freq([]) == {}

    def test_count_freq_case_sensitive(self):
        tokens = ["Word", "word", "WORD"]
        result = count_freq(tokens)
        # Предполагаем, что токены уже нормализованы
        assert result == {"Word": 1, "word": 1, "WORD": 1}


class TestTopN:
    """Тесты для функции top_n"""

    def test_top_n_basic(self):
        freq = {"a": 5, "b": 10, "c": 3, "d": 7}
        result = top_n(freq, 2)
        expected = [("b", 10), ("d", 7)]
        assert result == expected

    def test_top_n_tie_breaker(self):
        # Тест на случай одинаковой частоты (должна быть алфавитная сортировка)
        freq = {"z": 5, "a": 5, "m": 5, "b": 10}
        result = top_n(freq, 3)
        # b с самой высокой частотой, затем a, m, z с одинаковой частотой
        # но в алфавитном порядке: a, m, z
        expected = [("b", 10), ("a", 5), ("m", 5)]
        assert result == expected

    def test_top_n_more_than_available(self):
        freq = {"a": 1, "b": 2}
        result = top_n(freq, 5)
        expected = [("b", 2), ("a", 1)]
        assert result == expected

    def test_top_n_empty(self):
        assert top_n({}, 5) == []

    def test_top_n_zero(self):
        freq = {"a": 1, "b": 2}
        assert top_n(freq, 0) == []


class TestIntegration:
    """Интеграционные тесты для всего пайплайна"""

    def test_full_pipeline(self):
        text = "Привет мир! Мир привет всем. Всем привет еще раз."
        normalized = normalize(text)
        tokens = tokenize(normalized)
        freq = count_freq(tokens)
        top_words = top_n(freq, 2)

        assert normalized == "привет мир! мир привет всем. всем привет еще раз."
        assert "привет" in tokens
        assert "мир" in tokens
        assert freq["привет"] == 3
        assert freq["мир"] == 2
        assert top_words[0][0] == "привет"
