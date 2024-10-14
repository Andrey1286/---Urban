from math import *

class Figure:
    sides_count = 0
    def __init__(self, color,  *sides: int):
        self.__sides = list(sides)           # список сторон
        self.__color = list(color)           # список цветов
        self.filled = True                   # bool - тип данных, который может принимать True или False

    def get_color(self):
        return self.__color                  # возвращает список цветов

    def __is_valid_color(self, *rgb):
        if len(rgb) == 3:
            for i in (rgb):
                if 0 <= i <= 255:
                    return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print('Цвет остаётся прежним')

    def __is_valid_sides(self, *sides):
        for i in sides:
            if not isinstance(i, int) or i <= 0:
                return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):  # возвращает периметр фигуры
        if len(self.__sides) == 1:
            x = self.__sides[0]
        else:
            x = sum(self.__sides)
        return x  # периметр фигуры

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):
    sides_count = 1
    def __init__(self, color,  *sides):
        super().__init__(color,  *sides)
        if len(sides) == 1:
            self.__radius = sides[0] / (2 * pi)
        else:
            self.__radius = 1 / (2 * pi)

    def get_square(self):
        circle_area = pi * (self.__radius ** 2)
        return circle_area

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color,  *sides):
        super().__init__(color,  *sides)

    def get_square(self):
        p = self.__len__() / 2  # полупериметр
        a = self.get_sides()[0]  # длина первой стороны
        b = self.get_sides()[1]  # длина второй стороны
        c = self.get_sides()[2]  # длина третьей стороны
        circle_area = sqrt(p * (p - a) * (p - b) * (p-c))  # считаем площадь треугольнака по формуле Герона
        return circle_area

class Cube(Figure):
    sides_count = 12
    def __init__(self, color,  *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        else:
            sides = [1] * self.sides_count
        super().__init__(color,  *sides)


    def get_volume(self):
        cube_volume = self.get_sides()[0] ** 3
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

