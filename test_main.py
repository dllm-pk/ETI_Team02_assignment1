import pytest
import mainprog
import combat 


class test_main(unittest.TestCase) :

    @pytest.mark.parameterize()
    def test_town_menu():
        Enter(1)
        assert 
