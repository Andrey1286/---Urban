spisok1 = []

n = int(input('Введите число от 3 до 20: '))

cod = range(1, 20)

for i in range(len(cod)):
     for j in range(i + 1, len(cod)):
         sum1 = cod[i] + cod[j]
         if n % sum1 == 0:
             spisok1.append(str(cod[i]) + str(cod[j]))


spisok2 = int(''.join(spisok1))
print('Сгенерированный пароль:', spisok2)