the_board = {
    'top-L':' ','top-M':' ','top-R':' ',
    'mid-L':' ','mid-M':' ','mid-R':' ',
    'low-L':' ','low-M':' ','low-R':' ',
}
def print_board(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

print_board(the_board)
turn = 'X'
for i in range(9):
    pos = ''
    while True:
        if pos not in the_board.keys():
            print("Please input the right form of position")
            pos = input(f'Turn for {turn}.Move on which sapce?\n')
        else:
            if the_board[pos] != ' ':
                print('The space has been taken')
                pos = input(f'Turn for {turn}.Move on which sapce?\n')
            else:
                the_board[pos] = turn
                break
    if turn == 'X':
        turn = 'O'
    else:   
        turn = 'X'
    print_board(the_board)
