import pytest
from mainprog import *
import random

def test_orb():
    a = random.randint(1,5)
    b = random.randint(1,5)
    c = random.randint(1,5)
    test = [a,b,c]
    result = orb(a,b,c)
    original = [i-5 for i in result]
    assert test == original

def test_rest_day_passed():#HP will be fully healed
    day = random.randint(1,10) #Day passing
    result = rest(day,1,2)
    assert result[0] == day + 1

def test_rest_hpgap_lessthan20():#HP will be fully healed
    a = random.randint(1,10) #Current HP
    b = a + random.randint(1,20) #Max hp, any number less than or equals to 20
    result = rest(1,a,b)
    assert result[1] == b

def test_rest_hpgap_morethan20():#HP will be fully healed
    a = random.randint(1,10) #Current HP
    b = a + random.randint(20,35) #Max hp, any number less than or equals to 20
    result = rest(1,a,b)
    assert a + 20 == result[1]


      
       

        
