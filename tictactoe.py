
"""Tic Tac Toe is a game for two players. If all X's or all O's form a 
vertical,horizontal, or diagonal line, then the player with the X's or
O's wins the game. 
"""


def gameboard(list_x_o=None, win=None):
    """ This function prints out the gameboard."""
    if list_x_o is None:
        list_x_o = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    vertical_divide = "               |          |               "
    horizontal_divide = "       _____________________________"    
    print '\n' * 3
    print "Column    0          1          2          "
    print vertical_divide
    print "Row 0     %s    |     %s    |     %s          " % (list_x_o[0][0], list_x_o[0][1], list_x_o[0][2])
    print vertical_divide
    print horizontal_divide
    print vertical_divide                      
    print "Row 1     %s    |     %s    |     %s          " % (list_x_o[1][0], list_x_o[1][1], list_x_o[1][2])
    print vertical_divide
    print horizontal_divide
    print vertical_divide
    print "Row 2     %s    |     %s    |     %s         " % (list_x_o[2][0], list_x_o[2][1], list_x_o[2][2])  
    print vertical_divide  

    if win is True or win is False:
        start()
    else:
        new_value(list_x_o)


def new_value(list_x_o):
    """ This function asks the player which number they are and where they want to put their mark."""
    player_num = raw_input("Are you Player #1 or Player #2? (1/2) ")
    if player_num not in ['1', '2']:
        print "You are Player #1 or Player #2, please enter a 1 or 2 when asked your player number. "
        new_value(list_x_o)
    player_num = int(player_num)
    new_piece = raw_input("Where would you like to place your mark? (Row,Column) ")
    if "," not in new_piece:
        print "Please write in the coordinates of your mark separted by a comma."
        new_value(list_x_o)
    new_piece = new_piece.split(",")
    row = int(new_piece[0])
    column = int(new_piece[1])
    print new_piece
    place = list_x_o[row][column]

    if place == " ":
        mark(list_x_o, row, column, player_num)
    else:
        print "That space is already taken. Please pick another space for your mark. "
        new_value(list_x_o)


def mark(list_x_o, row, column, player_num):
    """This function puts the mark on the tic tac toe board"""
    if player_num == 1:
        list_x_o[row][column] = "X"
    elif player_num == 2:
        list_x_o[row][column] = "O"

    winner_check(list_x_o,player_num)  


def winner_check(list_x_o, player_num):
    """ This function checks to see if there is a winner or the  board is full"""
    print "checking for winner"
    if player_num == 1:
        mark = "X"
    else:
        mark = "O"
    condition = False

    # if list_x_o[0][0] == mark and list_x_o[0][1] == mark and list_x_o[0][2] == mark:
    #     condition = True
    # elif list_x_o[1][0] == mark and list_x_o[1][1] == mark and list_x_o[1][2] == mark:
    #     condition = True
    # elif list_x_o[2][0] == mark and list_x_o[2][1] == mark and list_x_o[2][2] == mark:
    #     condition = True
    # elif list_x_o[0][0] == mark and list_x_o[1][0] == mark and list_x_o[2][0] == mark:
    #     condition = True
    # elif list_x_o[0][1] == mark and list_x_o[1][1] == mark and list_x_o[2][1] == mark:
    #     condition = True
    # elif list_x_o[0][2] == mark and list_x_o[1][2] == mark and list_x_o[2][2] == mark:
    #     condition = True
    # elif list_x_o[0][0] == mark and list_x_o[1][1] == mark and list_x_o[2][2] == mark:
    #     condition = True
    # elif list_x_o[0][2] == mark and list_x_o[1][1] == mark and list_x_o[2][0] == mark:
    #     condition = True
    # print condition

    # could also be:
    for i in range(3):
        if list_x_o[i][0] == list_x_o[i][1] == list_x_o[i][2] == mark:
            condition = True
        elif list_x_o[0][i] == list_x_o[1][i] == list_x_o[2][i] == mark:
            condition = True
        elif list_x_o[0][0] == list_x_o[1][1] == list_x_o[2][2] == mark:
            condition = True
        elif list_x_o[0][2] == list_x_o[1][1] == list_x_o[2][0] == mark:
            condition = True
    print condition


    if condition is True:
        print "YOU WON!!!!!"
        gameboard(list_x_o, True)
    elif " " not in list_x_o[0] and " " not in list_x_o[1] and " " not in list_x_o[2]:
        print "No winners here"
        gameboard(list_x_o, False)
    else:
        gameboard(list_x_o)


def start():
    play = True
    while play:
        game_play = raw_input("Would you like to play tic tac toe (y/n)? ")
        game_play = game_play.lower()
        if game_play == "y":
            play = True
            gameboard()
        else:
            play = False


if __name__ == "__main__":
    start()



       