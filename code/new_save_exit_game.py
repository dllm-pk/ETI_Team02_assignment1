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
GAME_FILE_NAME = "C:\ETI\Testing\game_data.txt"

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
    TOWN_OPTIONS = [save_game, exit_new_game]
    town_menu()
    option = get_option(len(TOWN_OPTIONS))
    TOWN_OPTIONS[option-1](game)



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
    prompt="Enter choie ["+str(lower)+".."+str(upper)+"]: "
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

1) Save Game
2) Exit Game
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
    print(" Game Saved")
        
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
        

