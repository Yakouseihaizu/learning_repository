def list_to_str(list):
    string = ''
    for item in list:
        string += str(item)
    return string

def is_valid_chess_board(chess_board):
    b_piece = 0
    w_piece = 0
    b_king = 0
    w_king = 0
    posy_range = ['a','b','c','d','e','f','g','h']
    name_range = ['pawn','knight','bishop','rook','queen','king']

    for k,v in chess_board.items():
        try : 
            color = list(v)[0]
            name = list_to_str(list(v)[1:])
        except IndexError:
            print(f'check {k}, it may not have enough information')
            return False
        if color == 'b':
            b_piece+=1
            if b_king > 1:
                return False
            else:
                if name in name_range:
                    if name == 'king':
                        b_king += 1
                else :
                    return False
        elif color == 'w':
            w_piece+=1
            if w_king > 1:
                return False
            else:
                if name in name_range:
                    if name == 'king':
                        w_king += 1
                else :
                    return False
        else :
            return False
        
        if len(k) != 2:
            return False
        try :
            posx = int(list(k)[0])
            posy = list(k)[1]
        except ValueError:
            print(f'{k} is not the right form for the position')
            return False

        if posx > 8 or posx < 1:
            return False
        if posy not in posy_range:
            return False
    
    if b_king == 1 and w_king == 1:
        return True
        
    
chess_board = {'1h':'','6c':'wqueen','2g':'bbishop','5h':'bqueen','3e':'wking',}
if is_valid_chess_board(chess_board):
    print('True')
else:
    print('False')