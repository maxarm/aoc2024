import d03

def test_d03a_testdata():
    assert d03.get_mul_sum(True) == 161

def test_d03a_data():
    assert d03.get_mul_sum(False) == 161
