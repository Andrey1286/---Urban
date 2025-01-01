class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__sides = list(sides)  # список (длин) сторон (целые числа)
        self.__color = list(color)    # список цветов в формате RGB
        self.filled = True              # закрашенный

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return True

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = list((r, g, b))

    def __is_valid_sides(self, sides):
        list_of_parties = []
        for side in sides:
            if isinstance(side, int) and side > 0:
                list_of_parties.append(side)
        if len(list_of_parties) == len(sides) and len(list_of_parties) == self.sides_count:
            return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)  # возвращает периметр фигуры

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            counter = 0
            for side in new_sides:
                self.__sides[0 + counter] = side
                counter += 1


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * 3.14)  # посчитали радиус круга

    def get_square(self):  # возвращает площадь круга
        circle_area = 3.14 * (self.__radius ** 2)
        return circle_area


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):  # возвращает площадь треугольника
        p = 0.5 * sum(self.get_sides())  # считаем полупериметр
        triangle_area = (p * (p - self.get_sides()[0]) * (p - self.get_sides()[1]) * (p - self.get_sides()[2])) ** 0.5
        return triangle_area


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        if len(sides) == 1:
            sides = [sides[0]] * self.sides_count
        else:
            sides = [1] * self.sides_count
        super().__init__(color, *sides)

    def get_volume(self):                         # считаем объем куба
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
