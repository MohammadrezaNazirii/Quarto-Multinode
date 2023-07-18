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





def data_table(x, y, piece, lst1, lst2, lst3, lst4):
    if x == 1:
        lst1[y+(4*(y-1)):5*y] = list(piece)
    elif x == 2:
        lst2[y+(4*(y-1)):5*y] = list(piece)
    elif x == 3:
        lst3[y+(4*(y-1)):5*y] = list(piece)
    elif x == 4:
        lst4[y+(4*(y-1)):5*y] = list(piece)





def make_place_data(x, y, piece, by_row, by_column):
    by_column[y-1][x-1] = [piece]
    by_row[x-1][y-1] = [piece]
    return by_row, by_column





def possibility_row(by_row):
    for row in by_row:
        flag = True
        for piece in row:
            if piece == []:
                flag = False
                break
        if flag:
            break
    return flag, row





def possibility_column(by_column):
    for column in by_column:
        flag = True
        for piece in column:
            if piece == []:
                flag = False
                break
        if flag:
            break
    return flag, column





def check_winner(lst):
    if lst[0][0][0] == lst[1][0][0] == lst[2][0][0] == lst[3][0][0] or lst[0][0][1] == lst[1][0][1] == lst[2][0][1] == lst[3][0][1] or lst[0][0][2] == lst[1][0][2] == lst[2][0][2] == lst[3][0][2] or lst[0][0][3] == lst[1][0][3] == lst[2][0][3] == lst[3][0][3]:
        return True
    return False





def merge_dictionary(dict1, dict2):
    result = {}
    for key, value in dict1.items():
        if key in dict2.keys():
            result[key] = [dict1[key][0]+dict2[key][0], dict1[key][1]+dict2[key][1], dict1[key][2]+dict2[key][2]]
        else:
            result[key] = value

    for key, value in dict2.items():
        if key not in dict1.keys():
            result[key] = value

    return(result)





def descending(dictt):
    x = dictt
    y = len(dictt.keys())
    new_dict = {}
    while y > 0:
        maxx = 0
        i = 0
        for key, value in x.items():
            n = len(x.keys())
            if value[0] >= maxx:
                maxx = value[0]
                max_value = value
                kk = key
            i += 1
            if i == n:
                new_dict[kk] = max_value
        del x[kk]
                 
        y -= 1
    return new_dict
