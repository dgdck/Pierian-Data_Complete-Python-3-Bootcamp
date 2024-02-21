import random


def main():
    #display_board(test_board)
    #player_input()
    #place_marker(test_board, '@', 5)
    #win_board = ['#', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
    #print(win_check(win_board, 'X'))
    #print(go_first())
    #print(space_check(test_board, 4))
    #print(full_board_check(test_board))
    #print(player_choice(test_board))
    #print(replay())
    print('Welcome to Tic Tac Toe!')
    board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    while True:
        board = ['#'] + (9 * [' '])
        player1_marker, player2_marker = player_input()
        turn = go_first()
        print(f'{turn} will go first.')

        play_game = input('Are you ready to play? Enter Yes or No. ')
    
        if play_game.lower()[0] == 'y':
            game_on = True
        else:
            game_on = False
            break

        while game_on:
            if turn == 'Player 1':
                display_board(board)
                print(f'Player 1\'s turn: {player1_marker}')
                position = player_choice(board)
                place_marker(board, player1_marker, position)

                if win_check(board, player1_marker):
                    display_board(board)
                    print('Player 1 won!!!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a draw!')
                        game_on = False
                    else:
                        turn = 'Player 2'

            if turn == 'Player 2':
                display_board(board)
                print(f'Player 2\'s turn: {player2_marker}')
                position = player_choice(board)
                place_marker(board, player2_marker, position)

                if win_check(board, player2_marker):
                    display_board(board)
                    print('Player 2 won!!!')
                    game_on = False
                else:
                    if full_board_check(board):
                        display_board(board)
                        print('The game is a draw!')
                        game_on = False
                    else:
                        turn = 'Player 1'
        
        game_on = replay()
        if not game_on:
            break


test_board = ['#', 'X', ' ', 'O', 'O', 'O', 'O', 'X', 'O', 'X']


def display_board(board):
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


def player_input():
    player1 = ''
    player2 = ''
    menu = ['X', 'O']

    while player1 not in menu:

        player1 = input('Do you want to be X or O? ').upper()

        if player1 not in menu:
            print('\n' * 100)
            print('Sorry, please choose X or O.')

        if player1 in menu:
            if player1 == 'X':
                player1 = 'X'
                player2 = 'O'
            else:
                player1 = 'O'
                player2 = 'X'

    return (player1, player2)


def place_marker(board, marker, position):
    board[position] = marker

    return display_board(board)


def win_check(board, marker):
    wins = [marker, marker, marker]
    return (board[1:4] == wins or  # Across Bottom row
            board[4:7] == wins or  # Across Middle row
            board[7::] == wins or  # Across Top row
            (board[1] == marker and board[4] == marker and board[7] == marker) or  #  Left side
            (board[2] == marker and board[5] == marker and board[8] == marker) or  #  Down middle
            (board[3] == marker and board[6] == marker and board[9] == marker) or  #  Right side
            (board[7] == marker and board[5] == marker and board[3] == marker) or  #  Across from Top left
            (board[9] == marker and board[5] == marker and board[1] == marker))  # Across from top Right


def go_first():
    if random.randint(1, 100) % 2 == 0:
        return 'Player 1'
    else:
        return 'Player 2'


def space_check(board, position):
    return board[position] == ' '


def full_board_check(board):
    full_board = []

    for i in range(1, 9):
        full_board.append(space_check(board, i))

    return set(full_board) == {False}


def player_choice(board):
    # Step 8:
    # Write a function that asks for a player's next position (as a number 1-9)
    # then uses the function from step 6 to check if it's a free position.
    # If it is, then return the position for later use.
    position = 'wrong'
    while position not in range(1, 10):
        position = int(input('Where do you want to put your marker? (1-9) '))

        if position not in range(1, 10):
            print('Please choose position 1-9 ')

        elif space_check(board, position):
            return position
        else:
            print('Position is taken ')
            position = 'taken'


def replay():
    replay = "wrong"

    while replay not in ['y', 'n']:
        replay = input('Do you want to play again? Y/N ').lower()

        if replay not in ['y', 'n']:
            print('Please input Y or N ')

    return replay == 'y'


if __name__ == '__main__':
    main()
