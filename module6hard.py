from math import *

class Figure:
    sides_count = 0
    def __init__(self, color,  *sides):
        self.__sides = []
        self.__color = color           # список цветов
        self.filled = True  # bool - тип данных, который может принимать True или False

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in [r, g, b])

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            self.__color = self.__color
            print('Цвет остаётся прежним')

    def __is_valid_sides(self, *sides):
        if all(isinstance(side, int) and side > 0 for side in sides):
            return True
        else:
            False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print('Неверное количество или тип сторон')

class Circle(Figure):
    sides_count = 1
    def __init__(self, color,  *sides):
        pi = 3.14159
        super().__init__(color,  *sides)
        self.__radius = sides / (2 * pi)

    def get_square(self):
        pi = 3.14159
        circle_area = pi * self.__radius ** 2
        return circle_area

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color,  *sides):
        super().__init__(color,  *sides)

    def get_square(self):
        p = Figure.__len__() / 2  # полупериметр
        a = self.get_sides([0])
        b = self.get_sides([1])
        c = self.get_sides([2])
        circle_area = math.sqrt(p * (p - a) * (p - b) * (p-c))
        return circle_area

class Cube(Figure):
    sides_count = 12
    def __init__(self, color,  *sides):
        super().__init__(color,  *sides)
        self.side_length = self.get_sides([0])
        x = self.get_sides()
        for i in range(12):
            x.append(i)

    def get_volume(self):
        cube_volume = self.side_length ** 3
        return cube_volume

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

