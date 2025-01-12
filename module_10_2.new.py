import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name  # имя рыцаря
        self.power = power  # сила рыцаря
        self.number_of_enemies = 100  # количество врагов

    def run(self):
        print(f'{self.name}, на нас напали')
        counter = 0
        while self.number_of_enemies:
            self.number_of_enemies -= self.power
            time.sleep(1)
            counter += 1
            print(f'{self.name} сражается {counter} дней, осталось {self.number_of_enemies} воинов.')
        print(f'{self.name} одержал победу спустя {counter} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились')


