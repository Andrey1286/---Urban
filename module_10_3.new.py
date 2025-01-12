import threading
import time
import random


class Bank(threading.Thread):

    def __init__(self):
       super().__init__()
       self.balance = 0
       self.lock = threading.Lock()

    def deposit(self):
        self.lock.acquire()
        counter = 100
        while counter:
            replenishment = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                self.balance += replenishment
                print(f'Пополнение: {replenishment}. Баланс: {self.balance}.')
            time.sleep(0.0001)
            counter -= 1

    def take(self):
        counter = 100
        while counter:
            withdrawal = random.randint(50, 500)
            print(f'Запрос на {withdrawal}.')
            counter -= 1
            if withdrawal <= self.balance:
                self.balance -= withdrawal
                print(f'Снятие: {withdrawal}. Баланс: {self.balance}.')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()



bank = Bank()


thread1 = threading.Thread(target=bank.deposit)
thread2 = threading.Thread(target=bank.take)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print(f'Итоговый баланс: {bank.balance}')
