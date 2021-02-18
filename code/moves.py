from new_save_exit_game import *
from map import *
x = game[X_INDEX]
y = game[Y_INDEX]
msg = ""

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

#def move_up():
#    view_map(game)
#    position = 1
#    x = game[X_INDEX]
#    y = game[Y_INDEX]
#    game_map = game[MAP_INDEX]
#    n = len(game_map [0])
#    print()
#    msg = ""
#    bad = False
#    if x == 0:
#        bad == True
#        msg = "Cannot move UP"
#        print(msg)
#    else: 
#        x = x-1
#        msg = "Moved UP"
#    return [x, msg]
#    game[X_INDEX] = x
#    game[Y_INDEX] = y


#def move_down():
#    view_map(game)
#    position = 1
#    x = game[X_INDEX]   
#    y = game[Y_INDEX]
#    game_map = game[MAP_INDEX]
#    n = len(game_map [0])
#    print()
#    msg = ""
#    bad = False
#    if x == n-1:
#        bad == True
#        msg = "Cannot move DOWN"
#        print(msg)
#    else: 
#        x = x+1
#        msg = "Moved DOWN"
#    return [x, msg]
#    game[X_INDEX] = x
#    game[Y_INDEX] = y
