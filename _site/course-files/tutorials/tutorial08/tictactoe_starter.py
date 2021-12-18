game_data = [' '] * 9   # initialize game data to an empty array
player_symbol = 'o'     # TODO: make this customizable
computer_symbol = 'x'   # TODO: make this customizable
whose_turn = 'player'   # TODO: alternate between computer and player (within the loop)


def print_board(game_data):
    print()
    print('', game_data[6], '|', game_data[7], '|', game_data[8], '       7 | 8 | 9 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[3], '|', game_data[4], '|', game_data[5], '       4 | 5 | 6 ')
    print('-'* 11, '    ', '-'* 11)
    print('', game_data[0], '|', game_data[1], '|', game_data[2], '       1 | 2 | 3 ')
    print()


# keep looping until there's a winner:
while True:
    print_board(game_data)
    
    if whose_turn == 'player':

        selection = input('Where would you like to go (1-9 to play, Q to quit)? ')
        # --------------------------------------------------------------
        # # TODO: Complete Steps 1-3 for Tutorial 8
        # 1. if they typed 'q' or 'Q', break out of the loop
        # 2. check if the user entered a number between 1 and 9 
        #    Note: the code below will fail if the user enters a string.
        selection = int(selection) - 1
        # 3. make sure the number they picked isn't already taken


        # --------------------------------------------------------------
        game_data[selection] = player_symbol

        # after the user plays, switch to the computer's turn
        whose_turn = 'computer' 

    if whose_turn == 'computer':
        print('handle computer\'s turn')
        # TODO (for HW5): handle computer's turn:
        # your code here...

        # after the computer plays, switch to the player's turn
        whose_turn = 'player'


    # TODO (for HW5): each time either the computer plays, 
    #                 check if someone won or if there's a tie.