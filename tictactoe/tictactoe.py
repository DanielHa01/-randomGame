import random

def drawBoard(board):
    print('    |    |')
    print('  ' + board[7] + ' |  ' + board[8] + ' | ' + board[9])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print('  ' + board[4] + ' |  ' + board[5] + ' | ' + board[6])
    print('    |    |')
    print('--------------')
    print('    |    |')
    print('  ' + board[1] + ' |  ' + board[2] + ' | ' + board[3])
    print('    |    |')

def playerInput():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()
    
    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']

def firstTurn():
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def playAgain():
    print('Do you want to play again? (y or n)')
    return input().lower().startswith('y')

def makeMove(board, letter, move):
    board[move] = letter

def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))

def getBoardCopy(board):
    dupBoard = []

    for i in board:
        dupBoard.append(i)

    return dupBoard

def isSpaceValid(board, move):
    return board[move] == ' '

def getPlayerMove(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceValid(board, int(move)):
        print('What is your next move? (1-9)')
        move = input()
    return int(move)

def chooseRandomMoveFromList(board, moveList):
    possibleMoves = []
    for i in moveList:
        if isSpaceValid(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else: 
        return None

def getAIMove(board, AILetter):
    if AILetter == 'X':
        playerLetter == 'O'
    else: 
        playerLetter == 'X'

    for i in range(1, 10):
        dup = getBoardCopy(board)
        if isSpaceValid(dup, i):
            makeMove(dup, AILetter, i)
            if isWinner(dup, AILetter):
                return i
    
    for i in range(1, 10):
        dup = getBoardCopy(board)
        if isSpaceValid(dup, i):
            makeMove(dup, playerLetter, i)
            if isWinner(dup, playerLetter):
                return i

    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move

    if isSpaceValid(board, 5):
        return 5

    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceValid(board, i):
            return False
    return True

print ('Welcome to Tic Tac Toe!')

while True:
    board = [' '] * 10
    playerLetter, AILetter = playerInput()
    turn = firstTurn()
    print('The ' + turn + ' will go first.')
    gameIsPlaying = True

    while gameIsPlaying:
        if turn == 'player':
            drawBoard(board)
            move = getPlayerMove(board)
            makeMove(board, playerLetter, move)
            if isWinner(board, playerLetter):
                drawBoard(board)
                print("Congrats! You have won!")
                gameIsPlaying = False
            else:
                if isBoardFull(board):
                    drawBoard(board)
                    print('It\'s a tie!!!')
                    break
                else:
                    turn = 'computer'
        else:
            move = getAIMove(board, AILetter)
            makeMove(board, AILetter, move)
            if isWinner(board, AILetter):
                drawBoard(board)
                print("You lose!!! LOL")
                gameIsPlaying = False
            else: 
                if isBoardFull(board):
                    drawBoard(board)
                    print('It\'s a tie!!!')
                    break
                else:
                    turn = 'player'

    if not playAgain():
        break
