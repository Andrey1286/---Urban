import threading
import random
import time


class Bank:
    def __init__(self, balance=500):
        super().__init__()
        self.balance = balance
        self.lock = threading.Lock()

    def deposit(self):
        counter = 0
        self.lock.acquire()
        while counter < 101:
            random_number = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.balance += random_number
                print(f'Пополнение: {random_number}. Баланс: {self.balance}.')
            time.sleep(0.001)
            counter += 1
        self.lock.release()

    def take(self):
        counter = 0
        self.lock.acquire()
        while counter < 101:
            random_number_1 = random.randint(50, 500)
            print(f'Запрос на {random_number_1}.')
            if random_number_1 <= self.balance:
                self.balance -= random_number_1
                print(f'Снятие: {random_number_1}. Баланс: {self.balance}.')
            elif random_number_1 > self.balance:
                print(f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            counter += 1
        self.lock.release()


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
