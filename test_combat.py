
import pytest

@pytest.mark.one   
def test_attack():
        add(1)
        assert "You dealt 10 damange to the rat"

def test_flee():
    add(2)
    assert "You fled"
    
