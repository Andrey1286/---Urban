def password(n):
    soda = list(range(1,11))
    result = ''

    for i in range(len(soda)):
        for j in range(i, len(soda)):
            mixd = soda[i] + soda[j]
            if n % mixd == 0:
                result += str(soda[i]) + str(soda[j])
    return result

n = int(input('Введите число от 3 до 20: '))
soda1 = password(n)
print('Сгенерированный пароль:', soda1)
