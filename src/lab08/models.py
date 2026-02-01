from dataclasses import dataclass, field
from datetime import datetime, date
from typing import Self
import re


@dataclass
class Student:
    """Класс для представления студента."""
    
    fio: str
    birthdate: str
    group: str
    gpa: float
    
    def __post_init__(self) -> None:
        """Валидация данных после инициализации."""
        # Валидация ФИО
        if not self.fio or not isinstance(self.fio, str):
            raise ValueError("ФИО должно быть непустой строкой")
        
        # Валидация формата даты (YYYY-MM-DD)
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"Неверный формат даты: {self.birthdate}. Ожидается YYYY-MM-DD")
        
        # Валидация группы
        if not self.group or not isinstance(self.group, str):
            raise ValueError("Название группы должно быть непустой строкой")
        
        # Валидация среднего балла
        if not isinstance(self.gpa, (int, float)):
            raise ValueError("Средний балл должен быть числом")
        if not 0 <= self.gpa <= 5:
            raise ValueError(f"Средний балл должен быть в диапазоне 0-5, получено: {self.gpa}")
    
    def age(self) -> int:
        """Возвращает количество полных лет студента."""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        
        # Вычисляем разницу в годах
        age_years = today.year - birth_date.year
        
        # Корректируем, если день рождения в этом году ещё не наступил
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age_years -= 1
            
        return age_years
    
    def to_dict(self) -> dict:
        """Сериализует объект Student в словарь."""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> Self:
        """Десериализует объект Student из словаря."""
        # Проверяем обязательные поля
        required_fields = ["fio", "birthdate", "group", "gpa"]
        for field_name in required_fields:
            if field_name not in data:
                raise ValueError(f"Отсутствует обязательное поле: {field_name}")
        
        # Создаем объект Student
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=float(data["gpa"])
        )
    
    def __str__(self) -> str:
        """Возвращает строковое представление студента."""
        return (f"Студент: {self.fio}\n"
                f"Группа: {self.group}\n"
                f"Дата рождения: {self.birthdate} (Возраст: {self.age()} лет)\n"
                f"Средний балл: {self.gpa:.2f}")
    
    def __repr__(self) -> str:
        """Возвращает официальное строковое представление."""
        return (f"Student(fio='{self.fio}', birthdate='{self.birthdate}', "
                f"group='{self.group}', gpa={self.gpa})")