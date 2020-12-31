import unittest
import mainprog
import combat 
import pytest

class test_main(unittest.TestCase) :

    @pytest.mark.parameterize()
    def test_attack(min_damage,max_damage, defence):
        lose_hp = random.randint(min_damage,max_damage) - defence
        return lose_hp

    def test_flee():
        value=add(b)
        assert value == result
