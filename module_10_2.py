import threading
import time

class Knight(threading.Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        number_of_enemies = 100
        counter = 0
        while number_of_enemies > -1:
            number_of_enemies -= self.power
            counter += 1
            if number_of_enemies > 0:
                print(f'{self.name} сражается {counter} дней..., осталось {number_of_enemies} воинов.\n')
            elif number_of_enemies == 0:
                print(f'{self.name} одержал победу спустя {counter} дней(дня)!')
            time.sleep(1.0)

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()







