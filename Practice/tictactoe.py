THEBOARD = {'top-L':' ', 'top-R':' ','top-M':' ','mid-L':' ','mid-M':' ',
            'mid-R':' ', 'low-L':' ', 'low-R':' ','low-M':' '}

def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])

turn = 'X'
for i in range(9):
    printBoard(THEBOARD)
    print("Turn for " + turn + '. Move on which space?')
    move = input()
    THEBOARD[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(THEBOARD)



