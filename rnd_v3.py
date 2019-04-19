print('Было сгенерировано число от 1 до 15. Давай сыграем в угадайку :)')
import random
import sys
a = random.randint(1, 15)
counter = 3
print('У тебя есть', counter, 'попытки.')
print('Введите число от 1 до 15')
while counter != 0:
    b = int(input())    
    if b > 15 or b < 0:
        False
        print('Ты ввел не то число. Попробуй сыграть сначала')
        break              
    else:
        if a == b:
            print('Поздравляю, ты угадал! Действительно, искомое число было', a)
            break
            sys.exit()
        else:
            counter = counter - 1
            print('Попыток осталось:', counter)
if counter == 0:
    print('Ты проиграл. Загаданное число было', a)
input('Нажмите Enter чтобы продолжить')
