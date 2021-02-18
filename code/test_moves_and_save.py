
from new_save_exit_game import *
from map import *
from moves import *
import pytest
import random


def test_move_up_success():#Tests if moving up returns the correct x coordinate
    x = random.randint(1,7)#Positions on the map where moving up is possible
    result = move_up_success(x,y)
    assert result[0] == x-1

def test_move_up_failure():#Tests if failing to move up will return a message to prompt user
    result = move_up_failure(msg)#Message telling user the error
    assert result[0] == "Cannot move UP"

def test_move_down_success():#Tests if moving down returns the correct x coordinate
    x = random.randint(0,6)#Positions on the map where moving down is possible
    result = move_down_success(x,y)
    assert result[0] == x+1

def test_move_down_failure():#Tests if failing to move up will return a message to prompt user
    result = move_down_failure(msg)#Message telling user the error
    assert result[0] == "Cannot move DOWN"

def test_move_right_success():#Tests if moving right returns the correct y coordinate
    x = random.randint(0,6)#Positions on the map where moving right is possible
    result = move_right_success(x,y)
    assert result[1] == y+1

def test_move_right_failure():#Tests if failing to move up will return a message to prompt user
    result = move_right_failure(msg)#Message telling user the error
    assert result[0] == "Cannot move RIGHT"

def test_move_left_success():#Tests if moving left returns the correct y coordinate
    x = random.randint(1,7)#Positions on the map where moving left is possible
    result = move_left_success(x,y)
    assert result[1] == y-1

def test_move_left_failure():#Tests if failing to move up will return a message to prompt user
    result = move_left_failure(msg)#Message telling user the error
    assert result[0] == "Cannot move LEFT"

def test_save_game_game_state():#Tests if the correct game state is saved
    rat_hp = 10
    hero_hp = 20
    day = 1
    x = 0
    y = 0
    state = 0 #By default game state is 0
    result = save_game(game)
    assert result[0] == '0'

def test_save_game_hero_hp():#Tests if the correct hero hp is saved
    rat_hp = 10
    hero_hp = 20 #By default hero hp starts at 20
    day = 1
    x = 0
    y = 0
    state = 0
    result = save_game(game)
    assert result[1] == '20'

def test_save_game_day():#Tests if the correct day is saved
    rat_hp = 10
    hero_hp = 20
    day = 1 #By default day = 1
    x = 0
    y = 0
    state = 0
    result = save_game(game)
    assert result[2] == '1'

def test_save_game_rat_hp():#Tests if the correct rat hp is saved
    rat_hp = 10 #By default rat hp = 10
    hero_hp = 20
    day = 1
    x = 0
    y = 0
    state = 0
    result = save_game(game)
    assert result[3] == '10'

def test_save_game_x():#Tests if the correct x coordinate is saved
    rat_hp = 10
    hero_hp = 20
    day = 1
    x = 0 #By default x = 0
    y = 0
    state = 0
    result = save_game(game)
    assert result[4] == '0'

def test_save_game_y():#Tests if the correct y coordinate is saved
    rat_hp = 10
    hero_hp = 20
    day = 1
    x = 0
    y = 0 #By default y = 0
    state = 0
    result = save_game(game)
    assert result[5] == '0'