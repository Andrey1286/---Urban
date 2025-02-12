import threading
import time


def wite_words(word_count, file_name):
    counter = 0
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(word_count):
            counter += 1
            file.write(f'Какое-то слово № {counter}\n')
            time.sleep(0.1)
        print(f'Завершилась запись в файл {file_name}.')


start = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
final = time.time()
final_time = start - final
print(f'Работа потоков: {final_time} секунды')

start1 = time.time()
thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))

thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))

thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'))

thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'))


thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

final1 = time.time()
final_time1 = start1 - final1
print(f'Работа потоков: {final_time1} секунды')
