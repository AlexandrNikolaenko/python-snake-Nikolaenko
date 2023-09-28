from common.util import clear_terminal
from pynput import keyboard
from random import randint
from array import *

width, height = 20, 20

direction = (1, 0)

def generate_position():
    return randint(0, width - 1), randint(0, height - 1)

def process_press(key):
    # обработчик нажатия на клавиши (можно сделать и поаккуратнее)
    global direction
    match key:
        case keyboard.Key.left:
            direction = (0, -1)
        case keyboard.Key.up:
            direction = (-1, 0)
        case keyboard.Key.right:
            direction = (0, 1)
        case keyboard.Key.down:
            direction = (1, 0)

snake = (i, [[generate_position()]])
apple = generate_position()
body_snake = 0
new_elem = (snake[0][0] + direction[0], snake[0][1] + direction[1])

while apple in snake:
    apple = generate_position()

with keyboard.Listener(on_press=process_press) as listener:
    while True:
        clear_terminal()
        # рисуем змею и яблоко на поле
        field = [['.' for i in range(width)] for i in range(height)]
        for i in body_snake:
            if i == 0:
                field[snake[0][0]][snake[0][1]] = 'O'
            else:
                field[snake[i][0]][snake[i][1]] = 'o'
        field[apple[0]][apple[1]] = 'a'

        # выводим картинку

        for row in field:
            print(''.join(row))

        # передвигаем змею

        snake.insert(0, new_elem)

        if new_elem == apple:
            while apple in snake:
                apple = generate_position()
        else:
            snake.pop(-1)



