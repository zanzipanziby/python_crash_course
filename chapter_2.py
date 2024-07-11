# ГЛАВА 2. ПЕРЕМЕННЫЕ И ПРОСТЫЕ ТИПЫ ДАННЫХ
# СТРОКИ
# Вывод текста в разных регистрах
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

first_name = 'ada'
last_name = 'lovelace'
full_name = f'{first_name} {last_name}'
print('full name: ' + full_name)

# f-string
message = f'Hello {full_name.title()}'
print(message)

# Табуляции
print("Python")
print("\tPython")

# Разрывы строк
print("Languages: \n\tPython\n\tC\n\tJavaScript")

# Удаление пропусков
favorite_language = " Python "
print(favorite_language)  # " Python "
print(favorite_language.rstrip())  # " Python"
print(favorite_language.lstrip())  # "Python "
print(favorite_language.strip())  # "Python"
print(favorite_language == favorite_language.strip())  # False

# Предотвращение синтаксических ошибок в строках
# Для правильного определения строки использовать разные кавычки
message = "One of Python's favorite languages."

# ЧИСЛА
# Целые числа
print(2 + 3)  # 5
print(3 - 2)  # 1
print(2 * 3)  # 6
print(3 / 2)  # 1.5
print(3 ** 2)  # 9 Возведение в степень
print(3 - 2 * 2)  # -1
print((3 - 2) * 2)  # 2

# Вещественные числа
print(0.1 + 0.1)  # 0.2
print(0.2 + 0.2)  # 0.4
print(2 * 0.1)  # 0.2
print(2 * 0.2)  # 0.4

# Неожиданный результат из-за точного представления
print(0.2 + 0.1)  # 0.30000000000000004
print(3 * 0.1)  # 0.30000000000000004

# Целые и вещественные числа
# При делении и при операциях, в которых есть вещественное число, вы всегда получите вещественное число
print(4 / 2)  # 2.0
print(4.2 - 2.2)  # 2.0

# Символы подчеркивания в числах
# используются для группировки цифр в больших числах
universe_age = 14_000_000_000
print(universe_age)  # 14000000000

# Множественное присваивание
x, y, z = 1, 2, 3
print(x, y, z)  # 1 2 3

# Константы

MAX_CONNECTIONS = 5000
