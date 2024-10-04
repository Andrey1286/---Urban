master_code = 'Масетра кода'
data_wizards = 'Волшебники данных'
team1_num = 5
print('В команде %s участников: %s%s' % ('Мастера кода', 5, '!'))

team2_num = 5
team3_num = 6
print('Итого сегодня в командах участников: %(team2_num)s и %(team3_num)s!' % {'team2_num': 5, 'team3_num': 6})

score_2 = 42
print('Команда {} решила задач: {}!'.format(data_wizards, score_2))

team1_time = 1552.512
team2_time = 2153.31451
print('{} решили задачи за {} секунд!'.format(data_wizards, team1_time))

score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

challenge_result = 'Результат битвы'
if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды Волшебники данных!'
else:
    result = 'Ничья!'

print(f'{challenge_result}: {result}!')

tasks_total = 82
time_avg = 45.2
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')