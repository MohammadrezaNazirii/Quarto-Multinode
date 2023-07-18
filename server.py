from socketio import *
from gevent import pywsgi
from functions_server import *
import ast

server = Server(async_mode='gevent')

players = []
pieces = ['thd0', 'shl0', 'tfl0', 'shl4', 'tfl4', 'sfd0', 'thd4', 'tfd4', 'sfd4', 'shd4', 'shd0', 'thl4', 'sfl4', 'thl0', 'tfd0', 'sfl0']
s = '1100'
places = []
scoreboard = {}
scoreboard_list = []

with open('scoreboard.txt') as f:
    initial__dict = f.read()
initial_dict = ast.literal_eval(initial__dict)
usernames = []
for key in initial_dict.keys():
    usernames.append(key)


by_row = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
by_column = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
lst1 = ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|']
lst2 = ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|']
lst3 = ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|']
lst4 = ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|']
mohre = ''
status = ''

@server.event
def connect(sid, environ, auth):
    players.append(sid)
    print(sid, "connected!")
    server.emit('menu', data = [initial_dict, usernames], room = sid)

@server.event
def get_username(sid, data):
    global scoreboard_list
    if sid == players[0]:
        scoreboard_list = [data] + scoreboard_list
    else:
        scoreboard_list += [data]
    if len(scoreboard_list) == 2:
        server.emit('choose_mohre', data = pieces, room = players[0])
        print(scoreboard_list)
    scoreboard[data] = [0, 0, 0]

@server.event
def chosen_mohre(sid, data):
    global s ,mohre, temp
    mohre = create_mohre(data)
    pieces.remove(mohre)
    server.emit('choose_place', data = [lst1, lst2, lst3, lst4, mohre, data, places], room = players[int(s[0])])
    temp = int(s[0])
    s = s[1:]
    print('chosen_mohre DONE.')

@server.event
def chosen_place(sid, data):
    global s, by_row, by_column, possible_to_win, possible_to_lose, status
    data_table(data[0], data[1], mohre, lst1, lst2, lst3, lst4)
    
    places.append(data)
    
    by_row, by_column = make_place_data(data[0], data[1], mohre, by_row, by_column)
    
    flag, row = possibility_row(by_row)
    if flag:
        if not check_winner(row):
            by_row[by_row.index(row)] = [[], [], [], []]
            if len(pieces) == 0:
                status = 'draw'
                scoreboard[scoreboard_list[0]][2] += 1
                scoreboard[scoreboard_list[1]][2] += 1
                new_dict = descending(merge_dictionary(initial_dict, scoreboard))
                with open('scoreboard.txt', 'w') as f:
                    f.write(str(new_dict))
                server.emit('draw', data = [lst1, lst2, lst3, lst4, new_dict])
                return None
        else:
            scoreboard[scoreboard_list[possible_to_win]][0] += 1
            scoreboard[scoreboard_list[possible_to_lose]][1] += 1
            new_dict = descending(merge_dictionary(initial_dict, scoreboard))
            with open('scoreboard.txt', 'w') as f:
                f.write(str(new_dict))
            server.emit('win', data = [lst1, lst2, lst3, lst4, new_dict], room = players[possible_to_win])
            server.emit('lose', data = [lst1, lst2, lst3, lst4, new_dict], room = players[possible_to_lose])
            return None
    
    flag, column = possibility_column(by_column)
    if flag:
        if not check_winner(column):
            by_column[by_column.index(column)] = [[], [], [], []]
            if len(pieces) == 0:
                scoreboard[scoreboard_list[0]][2] += 1
                scoreboard[scoreboard_list[1]][2] += 1
                new_dict = descending(merge_dictionary(initial_dict, scoreboard))
                with open('scoreboard.txt', 'w') as f:
                    f.write(str(new_dict))
                server.emit('draw', data = [lst1, lst2, lst3, lst4, new_dict])
                return None
        else:
            scoreboard[scoreboard_list[possible_to_win]][0] += 1
            scoreboard[scoreboard_list[possible_to_lose]][1] += 1
            new_dict = descending(merge_dictionary(initial_dict, scoreboard))
            with open('scoreboard.txt', 'w') as f:
                f.write(str(new_dict))
            server.emit('win', data = [lst1, lst2, lst3, lst4, new_dict], room = players[possible_to_win])
            server.emit('lose', data = [lst1, lst2, lst3, lst4, new_dict], room = players[possible_to_lose])
            return None
    
    
    print('chosen_place DONE.')
    server.emit('choose_mohre', data = [pieces, lst1, lst2, lst3, lst4], room = players[int(s[0])])
    
    possible_to_lose = int(s[0])
    if possible_to_lose == 1:
        possible_to_win = 0
    else:
        possible_to_win = 1
    
    s = s[1:]
    if s == '':
        s = '1100'


@server.event
def start_new_game(sid, data):
    global s, mohre, scoreboard, pieces, places, by_row, by_column, lst1, lst2, lst3, lst4, status, initial_dict
    a = data
    with open('scoreboard.txt') as f:
        initial__dict = f.read()
    initial_dict = ast.literal_eval(initial__dict)
    pieces = ['thd0', 'shl0', 'tfl0', 'shl4', 'tfl4', 'sfd0', 'thd4', 'tfd4', 'sfd4', 'shd4', 'shd0', 'thl4', 'sfl4', 'thl0', 'tfd0', 'sfl0']
    s = '1100'
    places = []
    scoreboard = {}
    by_row = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
    by_column = [[[], [], [], []], [[], [], [], []], [[], [], [], []], [[], [], [], []]]
    lst1 = ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|']
    lst2 = ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|']
    lst3 = ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|']
    lst4 = ['|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|']
    mohre = ''
    server.emit('choose_mohre', data = pieces, room = players[0])
    if status == 'draw' and sid == players[0]:
        server.emit('welcome_to_new_game', data = 'Welcome to new game.', room = players[1])
        status = ''
    if status == 'draw' and sid == players[1]:
        server.emit('welcome_to_new_game', data = 'Welcome to new game.', room = players[0])
        status = ''
    scoreboard[scoreboard_list[0]] = [0, 0, 0]
    scoreboard[scoreboard_list[1]] = [0, 0, 0]



app = WSGIApp(server)

pywsgi.WSGIServer(("127.0.0.1", 5000), app).serve_forever()
