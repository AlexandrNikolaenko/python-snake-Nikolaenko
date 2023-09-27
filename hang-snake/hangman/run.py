from common.util import clear_terminal
from pynput import keyboard

secret_word = input('enter secret word').lower()

lose_field = r'''
   +----+
   |    |
   o    |
  /|\   |
  / \   |
_______/|\_
'''.split('\n')
loser = [
    (3, 3),
    (4, 3),
    (4, 2),
    (4, 4),
    (5, 2),
    (5, 4)
]
last_letter = []
picture = [list(row) for row in lose_field]
for i in loser:
    picture[i[0]][i[1]] = ' '

part_player = 0

n = len(secret_word)
enter_field = ['_' for _ in range(n)]

while True:
    clear_terminal()
    for row in picture:
        print(''.join(row))
    print()
    print()
    print(''.join(enter_field))
    letter = input('enter letter').lower()
    if ord(letter) < ord('a') or ord(letter) > ord('z') and len(letter) != 1:
        print('Error of the enter')
        continue
    elif letter in last_letter:
        print('This letter was already entered. Try other.')
        continue
    if letter in secret_word:
        for i in range(n):
            if secret_word[i] == letter:
                enter_field[i] = letter
    else:
        part = loser[part_player]
        picture[part[0]][part[1]] = lose_field[part[0]][part[1]]
        part_player += 1

    last_letter.append(letter)

    if len(loser) == part_player:
        print('You lose! Congratulations!')
        print()
        print('If you want to try again tap to space')
        break
    elif '_' not in enter_field:
        print('You won! Congratulations!')
        print()
        print('If you want to try again tap to escape')
        break