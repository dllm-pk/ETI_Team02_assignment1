from new_save_exit_game import *
import pytest
import random
import csv
import os
game = init_game()
def init_game():
    hero = get_new_hero()
    rat = get_new_rat()
    x = 0
    y = 0
    day = 1
    game = [IN_TOWN, DEFAULT_MAP, hero, day, rat, x, y]
    return game

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



