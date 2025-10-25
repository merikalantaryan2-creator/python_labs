m = int(input("Введите кол-во минут:"))

hours = m // 60
minutes = m % 60

print(f"{hours:02d}:{minutes:02d}")