#  Кэш игры.
score_1 = 0
score_2 = 0
player_1 = None
player_2 = None
check = None


#  Функция для визуального разделения строк.
def line_splitting():
    print('-------')
    return line_splitting


#  Функция для оттображения поля игры.
def print_matrix(matrix):
    line_splitting()
    for i in matrix:
        for j in i:
            print(j, end=' ')
        print()
    line_splitting()
    return print_matrix


#  Здесь написан ход игрока, где он вводит координаты клетки, функция проверяет эти координаты на коректность ввода и
#  проверяет не занята ли клетка "игровым символом". После хода идет проверка : есть ли на поле выиграшная комбинация.
def game_move(symbol, player, side):
    global move_x
    global game_matrix
    while True:
        print(f'Сейчас ходит {player} - {side}! ')
        while True:
            num_input_1 = input('Введите номер клетки по вертикали: ')
            num_input_2 = input('Введите номер клетки по горизонтали: ')
            if num_input_1.isdigit() and num_input_2.isdigit():
                a = int(num_input_1)
                b = int(num_input_2)
                break
            else:
                line_splitting()
                print('Введенны некоректные данные')
                line_splitting()
        if a < 1 > a > 3 or b < 1 or b > 3:
            line_splitting()
            print('Вы вышли за поле игры! Пожалуйста, введите коректные координаты нужной вам клетки.')
            print_matrix(game_matrix)
        elif '-' in game_matrix[a][b]:
            game_matrix[a][b] = symbol
            break
        else:
            line_splitting()
            print('Эта клетка уже занята! Пожалуйста, введите координаты нужной вам клетки.')
            print_matrix(game_matrix)
    print_matrix(game_matrix)
    check_winner(symbol, player)
    move_x += 1
    return move_x


#  Функция для проверки выиграшной комбинации, ксли ответ позитывный - увеличевает победный счет игрока.
def check_winner(symbol, player):
    global check
    global score_1
    global score_2
    check = 0
    if (game_matrix[1][1] == symbol and game_matrix[1][2] == symbol and game_matrix[1][3] == symbol) \
            or (game_matrix[2][1] == symbol and game_matrix[2][2] == symbol and game_matrix[2][3] == symbol) \
            or (game_matrix[3][1] == symbol and game_matrix[3][2] == symbol and game_matrix[3][3] == symbol) \
            or (game_matrix[1][1] == symbol and game_matrix[2][1] == symbol and game_matrix[3][1] == symbol) \
            or (game_matrix[1][2] == symbol and game_matrix[2][2] == symbol and game_matrix[3][2] == symbol) \
            or (game_matrix[1][3] == symbol and game_matrix[2][3] == symbol and game_matrix[3][3] == symbol) \
            or (game_matrix[1][1] == symbol and game_matrix[2][2] == symbol and game_matrix[3][3] == symbol) \
            or (game_matrix[1][3] == symbol and game_matrix[2][2] == symbol and game_matrix[3][1] == symbol):
        print(f'''Игра окончена!
{player} победил!''')
        if player == username:
            score_1 += 1
        else:
            score_2 += 1
        check += 1
    return check


#  Начало игры - Приветствие.
print('Добро пожаловать в игру Крестики-Нолики!')
line_splitting()
#
#
# Запрашиваем имя первого игрока и проверяем пустое поле.
username = input('Первый игрок, введите ваше имя : ')
while not username:
    line_splitting()
    username = input('''Имя игрока не может быть пустым!
Пожалуйста, введите ваше имя : ''')
line_splitting()
#
#
# Запрашиваем имя второго игрока и проверяем пустое поле.
username_2 = input('Второй игрок, введите ваше имя : ')
while not username_2:
    line_splitting()
    username_2 = input('''Имя игрока не может быть пустым!
Пожалуйста, введите ваше имя : ''')
line_splitting()
#
#
print(f'''{username} и {username_2}, я - разработчик этой игры - Тамплиер, приветствую вас!
P.S. На протяжении игры функция "изменить имя" - недоступна.''')
line_splitting()
#
#
# Начинается тело игры, выполняется бесконечный цикл для возможности постоянно начинать новую игру после окончания
# предидущей игры. Сначала спрашиваем игроком хотят ли они узнать правила и в каждой новой игре будет такая возможность.
while True:
    while True:
        while True:
            input_rules = input('''Если вы хотите узнать правила игры - напишите "1", и я вам их расскажу.
Если вы хотите сразу приступим к игре - напишите "2". 
Ваш ответ : ''')
            if input_rules.isdigit():
                rules = int(input_rules)
                if rules != 1 and rules != 2:
                    line_splitting()
                    print('Извените, я вас не понял.')
                    line_splitting()
                else:
                    break
            else:
                line_splitting()
                print('Введенны некоректные данные')
                line_splitting()
        if rules == 1:
            line_splitting()
            print('''   Игроки по очереди ставят на свободные клетки поля 3×3 знаки (один
всегда крестики, другой всегда нолики). Первый, выстроивший в ряд 3 своих
фигуры по вертикали, горизонтали или большой диагонали, выигрывает.
Если игроки заполнили все 9 ячеек и оказалось, что ни в одной вертикали,
горизонтали или большой диагонали нет трёх одинаковых знаков, партия
считается закончившейся в ничью.
    Первый ход делает игрок, ставящий крестики.''')
            line_splitting()
            break
        elif rules == 2:
            line_splitting()
            break
#
#
# Даём игроку возможность выбрать сторону и роспределяем игроком соответственно выбору.
    while True:
        while True:
            input_choice_of_side = input(f'''{username}, выберете за кого вы будете играть. 
Напишите "1" за Крестик, или "2" если за Нолик.
Ваш выбор : ''')
            if input_choice_of_side.isdigit():
                choice_of_side = int(input_choice_of_side)
                if choice_of_side != 1 and choice_of_side != 2:
                    line_splitting()
                    print('Извените, я вас не понял.')
                    line_splitting()
                else:
                    break
            else:
                line_splitting()
                print('Введенны некоректные данные')
                line_splitting()
        if choice_of_side == 1:
            player_1 = username
            player_2 = username_2
            break
        elif choice_of_side == 2:
            player_1 = username_2
            player_2 = username
            break
#
#
#  Оттображаем визуальное поле игры и выставляем начальное поле и начальный счетчик ходов.
    print(f'''Игра начинается!
    Вот как сейчас выглядит поле:''')
    game_matrix = [[' ', 1, 2, 3],
                   [1, '-', '-', '-'],
                   [2, '-', '-', '-'],
                   [3, '-', '-', '-']]
    print_matrix(game_matrix)
    move_x = 0
#
#
#  Цикл где игроки ходят попчереди пока полностью не заполнится поле или пока не будет выявлен победитель.
#  В конце отображается счёт игры.
    while True:
        game_move('x', player_1, 'Крестик')
        if check == 1:
            break
        if move_x == 9:
            print('Игра окончена ничьей!')
            break
        game_move('o', player_2, 'Нолик')
        if check == 1:
            break
    line_splitting()
    print(f'''Счет игры: {username} {score_1} : {score_2} {username_2}''')
    line_splitting()
#
#
#  Спрашиваем у игроков, хотят ли они начать новвую игру изи закончить играть.
    while True:
        restart_game_input = input(('''Если вы хотите начать новую игру - напишите "1"
Если вы хотите закончить игру - напишите "2"
Ваш выбор: '''))
        if restart_game_input.isdigit():
            restart_game = int(restart_game_input)
            if restart_game != 1 and restart_game != 2:
                line_splitting()
                print('Извените, я вас не понял.')
                line_splitting()
            else:
                break
        else:
            line_splitting()
            print('Введенны некоректные данные')
            line_splitting()
    if restart_game == 1:
        line_splitting()
        print("Отлично, приготовьтесь к новой игре.")
        line_splitting()
    else:
        line_splitting()
        print('Спасибо вам что сыграли в мою игру =) Буду ждать нашей следующей встречи =) ')
        line_splitting()
        break
