from new_save_exit_game import *
from map import *
x = game[X_INDEX]
y = game[Y_INDEX]
msg = ""

#Moves and results
def move_up_success(x,y):
    view_map(game)
    position = 1
    game_map = game[MAP_INDEX]
    n = len(game_map [0])
    print()
    x = x-1
    y = y
    return [x,y]

def move_up_failure(msg):
    view_map(game)
    position = 1
    game_map = game[MAP_INDEX]
    n = len(game_map [0])
    print()
    msg = "Cannot move UP"
    print(msg)
    return [msg]

def move_down_success(x,y):
    view_map(game)
    position = 1
    game_map = game[MAP_INDEX]
    n = len(game_map [0])
    print()
    x = x+1
    y = y
    return [x,y]


def move_down_failure(msg):
    view_map(game)
    position = 1
    game_map = game[MAP_INDEX]
    n = len(game_map [0])
    print()
    msg = "Cannot move DOWN"
    print(msg)
    return [msg]

def move_right_success(x,y):
    view_map(game)
    position = 1
    game_map = game[MAP_INDEX]
    n = len(game_map [0])
    print()
    x = x
    y = y+1
    return [x,y]

def move_right_failure(msg):
    view_map(game)
    position = 1
    game_map = game[MAP_INDEX]
    n = len(game_map [0])
    print()
    msg = "Cannot move RIGHT"
    print(msg)
    return [msg]

def move_left_success(x,y):
    view_map(game)
    position = 1
    game_map = game[MAP_INDEX]
    n = len(game_map [0])
    print()
    x = x
    y = y-1
    return [x,y]

def move_left_failure(msg):
    view_map(game)
    position = 1
    game_map = game[MAP_INDEX]
    n = len(game_map [0])
    print()
    msg = "Cannot move LEFT"
    print(msg)
    return [msg]


