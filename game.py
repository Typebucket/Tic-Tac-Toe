board = {'7':' ', '8':' ', '9':' ',
         '4':' ', '5':' ', '6':' ',
         '1':' ', '2':' ', '3':' '}

keys = []
for key in board:
    keys.append(key)

def print_board(board):
    print("|"+board['7']+'|'+board['8']+'|'+board['9']+'|')
    print(' -+-+-')
    print("|"+board['4']+'|'+board['5']+'|'+board['6']+'|')
    print(' -+-+-')
    print("|"+board['1']+'|'+board['2']+'|'+board['3']+'|')

def game():
    turn = "X"
    count = 0
    
    for i in range(10):
        print_board(board)
        print("Its your turn", turn, "Which plave do you want to move to:")
        move = input()
        if board[move] == ' ':
            board[move] = turn
            count += 1
        else:
            print("The place is already filles please take another move")
            continue
        if count >= 5:
            if board['7'] ==  board['8'] == board['9'] != ' ':
              print("Game is over")
              print_board(board)
              print("*******+", turn , "Won the game +*******")
              break
            elif board['4'] ==  board['5'] == board['6'] != ' ':
              print("Game is over")
              print_board(board)
              print("*******+", turn , "Won the game +*******")
              break
            elif board['1'] ==  board['2'] == board['3'] != ' ':
              print("Game is over")
              print_board(board)
              print("*******+", turn , "Won the game +*******")
              break
            elif board['1'] ==  board['4'] == board['7'] != ' ':
              print("Game is over")
              print_board(board)
              print("*******+", turn , "Won the game +*******")
              break
            elif board['2'] ==  board['5'] == board['8'] != ' ':
              print("Game is over")
              print_board(board)
              print("*******+", turn , "Won the game +*******")
              break
            elif board['3'] ==  board['6'] == board['9'] != ' ':
              print("Game is over")
              print_board(board)
              print("*******+", turn , "Won the game +*******")
              break
            elif board['7'] ==  board['5'] == board['3'] != ' ':
              print("Game is over")
              print_board(board)
              print("*******+", turn , "Won the game +*******")
              break
            elif board['1'] ==  board['5'] == board['9'] != ' ':
              print("Game is over")
              print_board(board)
              print("*******+", turn , "Won the game +*******")
              break
        if count == 9:
          print("Game Over, Its a Tie !")

        if turn == 'X':
          turn = 'O'

        else:
          turn = 'X'
    
    restart = input("Do you want to play again? Y/N: \n")
    if restart == "Y":
        for key in board:
            board[key]=' '
        game()

if __name__ == "__main__":
    game()