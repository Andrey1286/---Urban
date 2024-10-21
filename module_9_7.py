def is_prime(sum_three):
    def wrapper(*args, **kwargs):
        result_1 = sum_three(*args,**kwargs)
        for i in range(2, int(result_1 ** 0.5) + 1):
            if result_1 % i == 0:
                print('Составное')
                return result_1
        print('Простое')
        return result_1
    return wrapper

@is_prime
def sum_three(a, b, c):
    x = a + b + c
    return x

result = sum_three(25, 25, 25)
print(result)

