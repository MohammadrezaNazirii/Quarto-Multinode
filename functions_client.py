def print_table(lst1, lst2, lst3, lst4):
    s = '---------------------'
    print(s)
    for i in lst1:
        print(i, end = '')
    print()
    print(s)
    for i in lst2:
        print(i, end = '')
    print()
    print(s)
    for i in lst3:
        print(i, end = '')
    print()
    print(s)
    for i in lst4:
        print(i, end = '')
    print()
    print(s)





def print_help():
    print('----------------------------------------------')
    print('***How to play the game.***')
    print('1. You should select one feature of each tuple for a piece')
    print('    (tall, short)  (flat, hollow)  (dark, light)  (square, round)')
    print('2. For defining place of piece you should enter 2 numbers that are separated by space:')
    print('    First for row, Second for column.')
    print("Note: Numbering of rows and columns of game's board is like a matrix.")
    print()
    print('Game Play:')
    print('    The ﬁrst player selects one of the 16 pieces and gives it to his opponent.')
    print('    Second player places the piece on any square on the board;')
    print('    Second player must then choose one of the 15 pieces remaining and give it to his opponent.')
    print('    First player places the piece on a empty square, and so on...')
    print('Good Luck & Enjoy:)')
    print('----------------------------------------------')





def create_mohre(x):
    lst = x.split()
    s = ''
    if 'tall' in lst:
        s += 't'
    elif 'short' in lst:
        s += 's'
    
    if 'flat' in lst:
        s += 'f'
    elif 'hollow' in lst:
        s += 'h'
    
    if 'dark' in lst:
        s += 'd'
    elif 'light' in lst:
        s += 'l'
    
    if 'square' in lst:
        s += '4'
    elif 'round' in lst:
        s += '0'
    
    return s





def max_len(dictt):
    maxx = 0
    for key in dictt.keys():
        if len(key) > maxx:
            maxx = len(key)
    return maxx


def print_dictionary(dictt):
    if dictt == {}:
        print('The scoreboard is empty.')
    else:
        length = max_len(dictt) + 3
        print((length+1)*' ', '| Wins | Losses | Draws')
        for key in dictt.keys():
            length_value_win = len(str(dictt[key][0]))
            length_value_lose = len(str(dictt[key][1]))
            print(key, ((length)-len(key))*' ', '|', dictt[key][0], (3-length_value_win)*' ', '|', dictt[key][1], (5-length_value_lose)*' ', '|', dictt[key][2])





def print_menu():
    print('-----------------------')
    print('**MENU**')
    print('1. Play Game')
    print('2. Help')
    print('3. ScoreBoard')
    print('-----------------------')





def print_end_game():
    print('-----------------------')
    print('1. Start new game.')
    print('2. ScoreBoard')
    print('3. Exit')
