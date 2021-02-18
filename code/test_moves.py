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
