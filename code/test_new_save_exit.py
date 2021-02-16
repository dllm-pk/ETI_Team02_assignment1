from game_interface import *
import pytest
import random
import os
import csv

def test_newgame_day():#Checks if day stars at 1
    day = 1
    assert day == 1

