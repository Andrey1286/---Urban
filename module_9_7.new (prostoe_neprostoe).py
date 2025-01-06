def is_prime(func):
    def wrapper(*args):
        res = func(*args)
        for i in range(2, int(res ** 0.5) + 1):
            if res % i == 0:
                print('Составное')
                return res
        print('Простое')
        return res
    return wrapper

@is_prime
def sum_three(a, b, c):
    result1 = a + b + c
    return result1


result = sum_three(2, 0, 0)
print(result)
