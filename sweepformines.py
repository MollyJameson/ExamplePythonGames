"""
Sweep For Mines is a grid based game.
Each grid spot contains a number that represents
the number of neighbors tiles that could contain a mine.
The goal is to avoid selecting a mine tile.
"""
import random

# These globals can be tuned for "fun factor"
# for extra challenge add a state that asks these to be user configured.
# In the real game the grid is 10x10 with 10 mines.
GRID_WIDTH = 5
GRID_HEIGHT = 5
NUM_MINES = 5

# Gamestate consts
STATE_GAMEPLAY = 0
STATE_WIN = 1
STATE_LOSE = 2
STATE_QUIT = 3
CHAR_MINE = "*"
CHAR_EMPTY = "0"
CHAR_UNKNOWN = "?"


def get_y(index):
    return index / GRID_HEIGHT


def get_x(index):
    return index % GRID_WIDTH


def get_index(x, y):
    return (y * GRID_WIDTH) + x


def get_num_mines_around(index, board):
    checkx = get_x(index)
    checky = get_y(index)
    mines_found = 0
    for x in [checkx - 1, checkx, checkx + 1]:
        for y in [checky - 1, checky, checky + 1]:
            # Make sure valid grid positions
            if(x >= 0 and y >= 0 and
                    x < GRID_WIDTH and y < GRID_HEIGHT):
                if(board[get_index(x, y)] == CHAR_MINE):
                    mines_found += 1
    return mines_found


def generate_board(board, revealed_board):
    # In the real game it has some extra logic to verify that
    # The first click is never a mine, for simplicity that is left out here.
    # Generate an empty board. This will be flat list, not 2D and we will
    # convert the index.
    grid_total_spaces = (GRID_HEIGHT * GRID_WIDTH)
    # Clear from previous game possibly
    del board[:]
    del revealed_board[:]
    # Fill so we modify the reference. Workaround for not using "global" keyword
    board.extend([CHAR_EMPTY] * grid_total_spaces)
    revealed_board.extend([CHAR_UNKNOWN] * grid_total_spaces)
    mines_generated = 0
    # when debugging if you want the same game over and over again,
    # seed random with consistant number
    # random.seed(100)
    # We could do a shuffle here like in mastermind example, but as an
    # alternative
    while(mines_generated < NUM_MINES):
        randindex = random.randint(0, grid_total_spaces)
        # we have to check we didn't get the same number twice
        if(board[randindex] != CHAR_MINE):
            board[randindex] = CHAR_MINE
            mines_generated += 1
    # populate the numbers of neighbors to show
    for i in range(grid_total_spaces):
        if(board[i] != CHAR_MINE):
            board[i] = str(get_num_mines_around(i, board))


def show_board(show_all, board, revealed_board):
    print(' \n' * 25)
    # two spaces for the y labels
    strXLbls = "  "
    strLineBreak = "--"
    for i in range(GRID_WIDTH):
        strXLbls += str(i)
        strLineBreak += "-"
    print strXLbls
    print strLineBreak
    for y in range(GRID_HEIGHT):
        singleline = str(y) + "|"
        for x in range(GRID_WIDTH):
            if show_all:
                singleline += board[get_index(x, y)]
            else:
                singleline += revealed_board[get_index(x, y)]
        print singleline


def get_empty_neighbors_index_list(checkx, checky, board):
    neighbors = []
    for x in [checkx - 1, checkx, checkx + 1]:
        for y in [checky - 1, checky, checky + 1]:
            # Make sure valid grid positions
            if(x >= 0 and y >= 0 and
                    x < GRID_WIDTH and y < GRID_HEIGHT):
                index = get_index(x, y)
                neighbors.append(index)
    return neighbors


def player_turn_guess(board, revealed_board):
    show_board(False, board, revealed_board)
    str_input = raw_input("Input location guess (x,y), q to quit:")
    if(str_input == 'q'):
        return STATE_QUIT
    split_input = str_input.split(",")
    if(len(split_input) < 2):
        raw_input("Input 2 numbers, seperated by comma")
        return STATE_GAMEPLAY
    if(not split_input[0].isdigit() or not split_input[1].isdigit()):
        raw_input("Input 2 numbers, seperated by comma")
        return STATE_GAMEPLAY
    x = int(split_input[0])
    y = int(split_input[1])
    if(x < 0 or y < 0 or
       x >= GRID_WIDTH or y >= GRID_HEIGHT):
        raw_input("Numbers out of range")
        return STATE_GAMEPLAY
    index = get_index(x, y)
    revealed_board[index] = board[index]

    # lose if clicked on a mine
    if(revealed_board[index] == CHAR_MINE):
        show_board(False, board, revealed_board)
        raw_input("you lose " + str(x) + " " + str(y) + " was a mine")
        return STATE_LOSE

    # simplified flood fill algorithm for expanding path exploration.
    # reveal all empty neighbors all around empty grid spaces
    # up to containing a number
    if(board[index] == CHAR_EMPTY):
        visited_neighbor_list = []
        unvisited_neighbors_list = get_empty_neighbors_index_list(x, y, board)
        while(len(unvisited_neighbors_list) > 0):
            latest_index = unvisited_neighbors_list.pop(0)
            visited_neighbor_list.append(latest_index)
            revealed_board[latest_index] = board[latest_index]
            if(board[latest_index] == CHAR_EMPTY):
                latest_neighbors = get_empty_neighbors_index_list(
                    get_x(latest_index), get_y(latest_index), board)
                # we can't just use extend because need to that they haven't
                # already been visited
                for i in range(len(latest_neighbors)):
                    if(not latest_neighbors[i] in visited_neighbor_list and
                       not latest_neighbors[i] in unvisited_neighbors_list):
                        unvisited_neighbors_list.append(latest_neighbors[i])

    # Make our latest reveal go out in all directions until hitting a number
    # all zeros should be revealed.

    # win condition everything revealed, except num mines
    grid_total_spaces = GRID_WIDTH * GRID_HEIGHT
    total_revealed = 0
    for i in range(grid_total_spaces):
        if(board[i] != CHAR_MINE and revealed_board[i] != CHAR_UNKNOWN):
            total_revealed += 1
    if(total_revealed == grid_total_spaces - NUM_MINES):
        show_board(True, board, revealed_board)
        raw_input("YOU WIN")
        return STATE_WIN

    return STATE_GAMEPLAY


def start_new_game():
    board = []
    revealed_board = []
    generate_board(board, revealed_board)
    state = STATE_GAMEPLAY
    while(state == STATE_GAMEPLAY):
        state = player_turn_guess(board, revealed_board)
    return state

# Main entry point.
state = STATE_GAMEPLAY
while(state != STATE_QUIT):
    state = start_new_game()
