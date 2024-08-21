def generate_password(n):
    soda1 = []
    for i in range(1, n):
        for j in range(1, n):
            if n % (i + j) == 0:
                soda1.append(str(i) + str(j))
    result = ''.join(soda1)
    return result
n = int(input("Введите число от 3 до 20: "))
print("Пароль:", generate_password(n))
