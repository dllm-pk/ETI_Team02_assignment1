from new_save_exit_game import *
from map import *

#User inputs move
def get_move():
    moves = [W, A, S, D]
    
    while True:
        s = " "+W+ " = up; " + A+ " = left; " + S+ " = down; " + D+ " = right"
        print(s)
        prompt="Enter move: "
        move = input(prompt).upper()
        if move in moves: return move
        print("invalid input")

#Hero moves
def game_move(game):
    view_map(game)
    position = 1
    x = game[X_INDEX]
    y = game[Y_INDEX]
    game_map = game[MAP_INDEX]
    n = len(game_map [0])

    print()
    while True:
        move = get_move()
        bad = False
        if move == S:
            if x == n-1:
                bad = True
                print("Cannot move DOWN")
            else: x = x+1
        if move == W:
            if x == 0:
                bad = True
                print("Cannot move UP")
            else: x = x-1
        if move == D:
            if y == n-1:
                bad = True
                print("Cannot move RIGHT")
            else: y = y+1
        if move == A:
            if y == 0:
                bad = True
                print("Cannot move :LEFT")
            else: y = y-1
        if not bad: break
    game[X_INDEX] = x
    game[Y_INDEX] = y

def town_move(game):
    game_move(game)
    game[STATE_INDEX] = OUT_DOOR
    view_map(game)
    game[DAY_INDEX] = game[DAY_INDEX] + 1

town_move(game)