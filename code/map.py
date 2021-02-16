from new_save_exit_game import *

game = init_game()

def init_game():
    hero = get_new_hero()
    rat = get_new_rat()
    x = 0
    y = 0
    day = 1
    game = [IN_TOWN, DEFAULT_MAP, hero, day, rat, x, y]
    return game

DEFAULT_MAP = [
	[1, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 1, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 1, 0, 0],
	[0, 1, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0],
	[0, 0, 0, 0, 1, 0, 0, 0],
	[0, 0, 0, 0, 0, 0, 0, 0]
]

def view_map(game):
    print()
    game_map = game[MAP_INDEX]
    x = game[X_INDEX]
    y = game[Y_INDEX]
    n = len(game_map[0])
    s1 = "+"
    for i in range(n): s1 = s1 + "---+"
    print(s1)
    for i in range(n):
        s2 = "|"
        for j in range (n):
            s = ""
            if game_map[i][j]== 1:
                s = "T"
            if i == n-1 and j == n-1:
                s = "K"
            if x == i and y == j:
                if s =="": s = "H"
                else: s = s+"/H"
            if len(s) == 0: s = "   "
            if len(s) == 1: s = " "+s+" "
            s2 = s2 + s +"|"
        print(s2)
        print(s1)

view_map(game)