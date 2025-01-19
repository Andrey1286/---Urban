import multiprocessing
import time


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            if line.strip():  # проверка на пустые строки
                all_data.append(line)
    return all_data


if __name__ == '__main__':
    files = ['file1.txt', 'file2.txt', 'file3.txt', 'file4.txt']

    start = time.time()
    read_info('file1.txt')
    read_info('file2.txt')
    read_info('file3.txt')
    read_info('file4.txt')
    final = time.time()
    result_time = final - start
    print(f'Время выполнения функций линейным способом: {result_time}')

    start1 = time.time()
    process1 = multiprocessing.Process(target=read_info, args=('file1.txt',))
    process2 = multiprocessing.Process(target=read_info, args=('file2.txt',))
    process3 = multiprocessing.Process(target=read_info, args=('file3.txt',))
    process4 = multiprocessing.Process(target=read_info, args=('file4.txt',))

    process1.start()
    process2.start()
    process3.start()
    process4.start()

    process1.join()
    process2.join()
    process3.join()
    process4.join()

    final1 = time.time()
    result_time1 = final1 - start1
    print(f'Время выполнения функций при помощи процессов: {result_time1}')
