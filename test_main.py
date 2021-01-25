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


      
       

        
