
import pytest
from full_program import *

@pytest.mark.one   
def test_attack(outdoor_attack):
    add(1)
    option = get_option(1)
    COMBAT_OPTIONS[option-1](game)

def test_flee(outdoor_run):
    add(2)
    assert "You fled"
    
