import random


class Animal:  # класс описывающий животных
    live = True  # живой
    sound = None  # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0  # степень опасности существа

    def __init__(self, speed):
        self._cords = [0, 0, 0]  # координаты в пространстве
        self.speed = speed  # скорость передвижения существа

    def move(self, dx, dy, dz):
        new_z_coordinate = self._cords[2] + self.speed * dz
        if new_z_coordinate < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[2] = new_z_coordinate
            self._cords[0] += self.speed * dx
            self._cords[1] += self.speed * dy

    def get_cords(self):
        print(f'X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Sorry, i am peaceful :)')
        elif self._DEGREE_OF_DANGER >= 5:
            print('Be careful, i am attacking you 0_0')

    def speak(self):
        print(f'{self.sound}')


class Bird(Animal):
    beak = True  # наличие клюва

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        print(f'Here are(is) {random.randint(1, 4)} eggs for you')


class AquaticAnimal(Animal):  # описывает плавающих животных
    _DEGREE_OF_DANGER = 3

    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):  # dz - изменение координаты z в _cords
        new_z_coordinate = self._cords[2] - abs(dz) * self.speed / 2
        self._cords[2] = new_z_coordinate


class PoisonousAnimal(Animal):  # класс описывающий ядовитых животных
    _DEGREE_OF_DANGER = 8

    def __init__(self, speed):
        super().__init__(speed)


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):  # класс описывающий утконоса
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = "Click-click-click"


db = Duckbill(10)


print(db.live)

print(db.beak)


db.speak()

db.attack()


db.move(1, 2, 3)

db.get_cords()

db.dive_in(6)

db.get_cords()


db.lay_eggs()
