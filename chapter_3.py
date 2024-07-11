# ГЛАВА 3. СПИСКИ
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[-1])  # specialized, последний элемент списка(первый с конца)
print(bicycles[-2])  # redline, предпоследний элемент списка(второй с конца)

# Использование отдельных элементов списка
message = f"My first bicycles was a {bicycles[0].title()}"
print(message)

# ИЗМЕНЕНИЕ, ДОБАВЛЕНИЕ И УДАЛЕНИЕ ЭЛЕМЕНТОВ
# ИЗМЕНЕНИЕ
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# ДОБАВЛЕНИЕ
motorcycles.append('jawa')  # добавляет в конец списка
print(motorcycles)
motorcycles.insert(0, 'izh')  # добавление по индексу, последующие сдвигаются.
print(motorcycles)

# УДАЛЕНИЕ
# с использованием del
del motorcycles[0]  # Удаляет 1 элемент
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki', 'jawa']

# метод pop()
popped_motorcycles = motorcycles.pop()  # Удаляет и возвращает последний элемент списка
print(popped_motorcycles)  # jawa
print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop(0)  # Удаляет и возвращает элемент списка по переданному индексу
print(popped_motorcycles)  # ducati
print(motorcycles)  # ['yamaha', 'suzuki']

# Удаление по значению
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.remove('yamaha')
print(motorcycles)

# Упорядочение списка
# Постоянная сортировка методом sort() (список мутирует)
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']
cars.sort(reverse=True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']

# Временная сортировка функцией sorted() (список не мутирует)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyota']
print(sorted(cars, reverse=True))  # ['toyota', 'subaru', 'bmw', 'audi']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

# Вывод в обратном порядке  reverse() (мутирует список)
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
cars.reverse()
print(cars)  # ['subaru', 'toyota', 'audi', 'bmw']

# Определение длины списка
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))  # 4
print(cars[len(cars) - 1])  # subaru (вывод последнего элемента)

# Ошибки индексирования при работе со списком
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[3])  # IndexError: list index out of range
motorcycles = []
print(motorcycles[-1])  # IndexError: list index out of range (ошибка только при пустом списке)
