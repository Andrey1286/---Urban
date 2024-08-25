# a = message
# b = recipient
# с = sender

def send_email(a, b, *, c='university.help@gmail.com'):
    if '@' in b and ('.com' in b or '.ru' in b or '.net' in b):
        if '@' in c and ('.com' in c or '.ru' in c or '.net' in c):
            if c == b:
                print('Нельзя отправить письмо самому себе!')
                return
            if c == 'university.help@gmail.com':
                print('Письмо успешно отправлено с адреса', c, 'на адрес', b)
                return
            else:
                print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', c, 'на адрес', b)
                return
        else:
            print('Невозможно отправить письмо с адреса', c, 'на адрес', b)
            return


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', c ='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', c ='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', c ='urban.teacher@mail.ru')