import pytest
from full_program import *

@pytest.mark.parametrize()
def test_enter_town():
    TOWN_OPTIONS= int(1)
    assert "You are in a town"

def test_view_character(game):
    hero = game[HERO_INDEX]
    
    assert("The Hero")
    assert("  Damage:", hero, "-", hero)
    assert(" Defence:", hero)
    assert("      HP:", hero)
      
       

        
