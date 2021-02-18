import random
import csv
import os

################################
# Parameters
################################
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
HERO_MIN_DAMAGE = 2
HERO_MAX_DAMAGE = 4
HERO_DEFENCE = 1
HERO_REST_HP = 20
RAT_MIN_DAMAGE = 1
RAT_MAX_DAMAGE = 3
RAT_DEFENCE = 1
RAT_REST_HP = 10

UP = "W"
LEFT = "A"
DOWN = "S"
RIGHT = "D"

IN_TOWN = 0
OUT_DOOR = 1
COMBAT = 2
QUIT_GAME = 3
HERO_DEAD = 4
WIN = 5

STATE_INDEX = 0
MAP_INDEX = 1
HERO_INDEX = 2
DAY_INDEX = 3
RAT_INDEX = 4
X_INDEX = 5
Y_INDEX = 6


WELCOME_MSG = "Welcome to Ratventure!"
GAME_FILE_NAME = "C:\ETI\Rat\game_data.txt"

################################
# game control
################################
def new_game():
    ''' 
Start a new Game
    '''
    game = init_game()
    game_control(game)
    
def init_game():
    hero = get_new_hero()
    rat = get_new_rat()
    x = 0
    y = 0
    day = 1
    game = [IN_TOWN, DEFAULT_MAP, hero, day, rat, x, y]
    return game

def game_control(game):
    while True:
        state = game[STATE_INDEX]
        if state == IN_TOWN:
            town_menu_control(game)
        elif state == OUT_DOOR:
            outdoor_menu_control(game)
        elif state == COMBAT:
            combat_menu_control(game)
        elif state == HERO_DEAD:
            print("Hero is dead!")
            break
        elif state == QUIT_GAME:
            break
        elif state == WIN:
            break
        
def town_menu_control(game):
    ''' 
Control game function when the hero is at town
    '''
    day = game[DAY_INDEX]
    print("Day " + str(day)+ ": You are in a town.")
    TOWN_OPTIONS = [view_character, view_map, town_move, rest,
                        save_game, exit_new_game]
    town_menu()
    option = get_option(len(TOWN_OPTIONS))
    TOWN_OPTIONS[option-1](game)
     
def combat_menu_control(game):
    day = game[DAY_INDEX]
    print("Day " + str(day)+ ": You are out in the open")
    view_character(game)
    print("Encounter! - Rat")
    view_rat(game)
    combat_menu()
    COMBAT_OPTIONS = [outdoor_attack, outdoor_run]
    option = get_option(len(COMBAT_OPTIONS))
    COMBAT_OPTIONS[option-1](game)

def outdoor_menu_control(game):
    OUTDOOR_OPTIONS = [view_character, view_map, outdoor_move, exit_outdoor_game]
    outdoor_menu()
    option = get_option(len(OUTDOOR_OPTIONS))
    OUTDOOR_OPTIONS[option-1](game)

def start():
    ''' 
Start the Ratventure Game
    '''
    MAIN_OPTIONS = [new_game, resume_game, exit_game]
    print(WELCOME_MSG)
    while True:
        main_menu()
        option = get_option(len(MAIN_OPTIONS))
        MAIN_OPTIONS[option-1]()
        
# Data Structure 

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

###################################
#    utility functions
###################################

def get_option(upper, lower = 1):
    ''' 
Purpose: Interactively get an option in a specific range.
Parameters: 
	lower: lower bound of the range
	upper: upper bound of the range
Return: An integer in [lower .. (upper-1)].
    '''
    prompt="Enter choice ["+str(lower)+".."+str(upper)+"]: "
    while True:
        input_str = input(prompt)
        try:
           input_num = int(input_str)
           if input_num in range(lower, upper+1): 
           	return input_num
           print("input number is not in range")
        except ValueError:
           print("input not an integer!")
           
def get_new_hero():
    hero = [HERO_MIN_DAMAGE, HERO_MAX_DAMAGE, HERO_DEFENCE, HERO_REST_HP]
    return hero

def get_new_rat():
    rat= [RAT_MIN_DAMAGE, RAT_MAX_DAMAGE, RAT_DEFENCE, RAT_REST_HP]
    return rat

def view_rat (game):
    rat = game[RAT_INDEX]
    print("  Damage:", rat[0], "-", rat[1])
    print(" Defence:", rat[2])
    print("      HP:", rat[3])

def get_move():
    moves = [UP, LEFT, DOWN, RIGHT]
    
    while True:
        s = " "+UP+ " = up; " + LEFT+ " = left; " + DOWN+ " = down; " + RIGHT+ " = right"
        print(s)
        prompt="Enter move: "
        move = input(prompt).upper()
        if move in moves: return move
        print("invalid input")
      
def update_damage(hero_rat, damage):
    damage = damage - hero_rat[2]
    if damage > 0: hero_rat[3] = hero_rat[3] - damage

def dead(hero_rat):
    return hero_rat[3] <= 0

def in_town(game):
    x = game[X_INDEX]
    y = game[Y_INDEX]
    game_map= game[MAP_INDEX]
    return game_map[x][y] == 1

def win_game(game):
    x = game[X_INDEX]
    y = game[Y_INDEX]
    game_map= game[MAP_INDEX]
    n = len(game_map[0])
    return x == n-1 and y == n-1   


###################################
# Game functions
###################################

def view_character(game):
    hero = game[HERO_INDEX]
    print()
    print("The Hero")
    print("  Damage:", hero[0], "-", hero[1])
    print(" Defence:", hero[2])
    print("      HP:", hero[3])
    
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
        if move == DOWN:
            if x == n-1:
                bad = True
                print("Cannot move DOWN")
            else: x = x+1
        if move == UP:
            if x == 0:
                bad = True
                print("Cannot move UP")
            else: x = x-1
        if move == RIGHT:
            if y == n-1:
                bad = True
                print("Cannot move RIGHT")
            else: y = y+1
        if move == LEFT:
            if y == 0:
                bad = True
                print("Cannot move :LEFT")
            else: y = y-1
        if not bad: break
    game[X_INDEX] = x
    game[Y_INDEX] = y

def town_move(game):
    game_move(game)
    if win_game(game):
        game[STATE_INDEX] = WIN
        print("You found the Orb of Power!!!")
        return
    game[RAT_INDEX] = get_new_rat()
    game[STATE_INDEX] = COMBAT
    view_map(game)
    game[DAY_INDEX] = game[DAY_INDEX] + 1

def outdoor_move(game):
    game_move(game)
    if win_game(game):
        game[STATE_INDEX] = WIN
        print("You found the Orb of Power!!!")
        return
    if in_town(game):
        game[STATE_INDEX] = IN_TOWN
        game[RAT_INDEX] = get_new_rat()
    else: game[STATE_INDEX] = COMBAT
    view_map(game)
    game[DAY_INDEX] = game[DAY_INDEX] + 1
    
def rest(game):
    game[DAY_INDEX] = game[DAY_INDEX] + 1
    game[HERO_INDEX][3]=HERO_REST_HP
    print("Day " + str(game[DAY_INDEX])+ ": You are fully healed.")

def outdoor_attack(game):
    hero = game[HERO_INDEX]
    min_damage = hero[0]
    max_damage = hero[1]
    damage = random.randrange(min_damage, max_damage+1)
    rat = game[RAT_INDEX]
    update_damage(rat, damage)
    if dead (rat):
        print("The rat is terminated!")
        game[STATE_INDEX] = OUT_DOOR
        game[RAT_INDEX] = get_new_rat()
        return
    min_damage = rat[0]
    max_damage = rat[1]
    damage = random.randrange(min_damage, max_damage+1)
    update_damage(hero, damage)
    if dead (hero):
        game[STATE_INDEX] = HERO_DEAD

def outdoor_run(game):
    print("You run and hide.")
    game[STATE_INDEX] = OUT_DOOR
    game[DAY_INDEX] = game[DAY_INDEX] + 1
    game[RAT_INDEX] = get_new_rat()
    print("Day " + str(game[DAY_INDEX])+ ": You are out in the open")
        
###################################
# Menus
###################################
def  main_menu():
    ''' 
Display the main menu for the Game
    '''
    print("""
Main Menu
----------------------
1) New Game
2) Resume Game
3) Exit Game
""")

def  town_menu():
    ''' 
Display the town menu for the Game
    '''
    print("""
Town Menu
----------------------
1) View Character
2) View Map
3) Move
4) Rest
5) Save Game
6) Exit Game
""")

def  outdoor_menu():
    ''' 
Display the outdoor menu for the Game
    '''
    print("""
Out door Menu
----------------------
1) View Character
2) View Map
3) Move
4) Exit Game
""")

def  combat_menu():
    ''' 
Display the outdoor menu for the Game
    '''
    print("""
Combat Menu
----------------------
1) Attack
2) Run
""")

####################################
# Game control: start, new, resume, exit
###################################

    	
def save_game(game):
    rat_hp = str(game[RAT_INDEX][3])
    hero_hp = str(game[HERO_INDEX][3])
    day = str(game[DAY_INDEX])
    x = str(game[X_INDEX])
    y = str(game[Y_INDEX])
    state = str(game[STATE_INDEX])
    
    game_data = [state, hero_hp, day, rat_hp, x, y]
    game_file = open(GAME_FILE_NAME, 'w')
    for x in game_data:
        game_file.write(x)
        game_file.write("\n")
    game_file.close()
    print(" Game saved")
        
def resume_game():
    ''' 
Resume the saved game from file
    '''
    game_file=open(GAME_FILE_NAME,'r')
    game_data = list(game_file)
    hero = get_new_hero()
    rat = get_new_rat()
    
    state = int(game_data[0])
    hero[3] = int(game_data[1])
    day = int(game_data[2])
    rat[3] = int(game_data[3])
    x = int(game_data[4])
    y = int(game_data[5]) 
    game = [state, DEFAULT_MAP, hero, day, rat, x, y]
    game_control(game)
           
def exit_game():
    ''' 
Print a thank you message before exit from the game
    '''
    print()
    print("Thank you for playing the game")
    print("Have a good day")
    print("Bye")
    quit()

def exit_new_game(game):
    s = input("Save game before quit [Y|N]?").upper()
    if s == "Y": save_game(game)
    game[STATE_INDEX] = QUIT_GAME
    print("You quit the game")

def exit_outdoor_game(game):
    game[STATE_INDEX] = QUIT_GAME
    print("You quit the game")

###################################      
# Launch the system
###################################

if __name__ == "__main__":
    print(__name__)
    start()
    input("Hit return to exit")
        
