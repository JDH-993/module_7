from os import times

team1_num = int(input())
team2_num = int(input())
score_1 = int(input())
score_2 = int(input())
team1_time = float(input())
team2_time = float(input())

tasks_total = score_1 + score_2
time_avg = (team1_time + team2_time)/tasks_total

challenge_result = None

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастеракода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    challenge_result = 'Ничья!'

print('"В команде матеракода участников: %s !"' % team1_num)
print('"Итого сегодня в командах участников: %s и %s !"' % (team1_num,  team2_num))
print('"Команда Волшебники данных решила задач: {}"'.format(score_2))
print('"Волшебники данных решили задачи за {} с !"'.format(team1_time))
print(f'"Команды решила: {score_1} и {score_2}!"')
print(f'""Результат битвы:{challenge_result}"')
print(f'"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!."')