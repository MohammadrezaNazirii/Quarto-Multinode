from socketio import *

from functions_client import *


client = Client()

@client.event
def menu(data):
    while True:
        print_menu()
        i = input('What do you want to do? ')
        print('-----------------------')
        if i == '1':
            print('Selected usernames:')
            print(data[1])
            username = input('Enter your User Name for scoreboard: ')
            client.emit('get_username', data = username)
            break
        elif i == '2':
            print_help()
        elif i == '3':
            print_dictionary(data[0])

@client.event
def choose_mohre(data):
    if data != ['thd0', 'shl0', 'tfl0', 'shl4', 'tfl4', 'sfd0', 'thd4', 'tfd4', 'sfd4', 'shd4', 'shd0', 'thl4', 'sfl4', 'thl0', 'tfd0', 'sfl0']:
        lst1 = data[1]
        lst2 = data[2]
        lst3 = data[3]
        lst4 = data[4]
        print_table(lst1, lst2, lst3, lst4)
        print('Remaining pieces:', data[0])
        pieces = data[0]
    else:
        print('Remaining pieces:', data)
        pieces = data
    while True:
        flag = True
        mohre = input('Please choose one piece... ')
        mohre = mohre.lower()
        for i in mohre.split():
            if i not in ['tall', 'short', 'flat', 'hollow', 'dark', 'light', 'square', 'round']:
                flag = False
                break
        if flag:
            piece = create_mohre(mohre)
            if piece in pieces:
                break
            print('Invalid input. Please choose another piece.')
        else:
            print('Invalid input. Please choose another piece.')
    print('Wait for your opponent...')
    client.emit('chosen_mohre', data = mohre)

@client.event
def choose_place(board):
    lst1 = board[0]
    lst2 = board[1]
    lst3 = board[2]
    lst4 = board[3]
    print("Your opponent's chosen piece is", board[5], 'or', board[4])
    print_table(lst1, lst2, lst3, lst4)
    while True:
        xy = input('Please enter place of next piece: ').split()
        if len(xy) == 2:
            x, y = xy
            if x.isdigit() and y.isdigit():
                place = [int(x), int(y)]
                if 1 <= int(x) <= 4 and 1 <= int(y) <= 4:
                    if place not in board[6]:
                        break
        print('Invalid input. Please choose another place.')
    
    client.emit('chosen_place', data = place)

@client.event
def win(data):
    lst1 = data[0]
    lst2 = data[1]
    lst3 = data[2]
    lst4 = data[3]
    print_table(lst1, lst2, lst3, lst4)
    print('You won.')
    while True:
        print_end_game()
        a = input('What do you want to do? ')
        print('-----------------------')
        if a == '1':
            client.emit('start_new_game', data = a)
            break
        elif a == '2':
            print_dictionary(data[4])
        elif a == '3':
            print('See you next time:)')
            break

@client.event
def lose(data):
    lst1 = data[0]
    lst2 = data[1]
    lst3 = data[2]
    lst4 = data[3]
    print_table(lst1, lst2, lst3, lst4)
    print('You lost.')
    while True:
        print_end_game()
        a = input('What do you want to do? ')
        print('-----------------------')
        if a == '1':
            print('Winner decides for new game.')
            print('Wait for your opponent...')
            break
        elif a == '2':
            print_dictionary(data[4])
        elif a == '3':
            print('See you next time:)')
            break
    

@client.event
def draw(data):
    lst1 = data[0]
    lst2 = data[1]
    lst3 = data[2]
    lst4 = data[3]
    print_table(lst1, lst2, lst3, lst4)
    print('Draw! Nobody wins.')
    while True:
        print_end_game()
        print('')
        a = input('What do you want to do? ')
        print('-----------------------')
        if a == '1':
            client.emit('start_new_game', data = a)
            print('Wait for your opponent...')
            break
        elif a == '2':
            print_dictionary(data[4])
        elif a == '3':
            print('See you next time:)')
            break
        elif a == '4':
            break


@client.event
def welcome_to_new_game(data):
    print(data)
    print('You are entered new game. Please press 4 to continue and start the game... ')

client.connect("http://127.0.0.1:5000")
