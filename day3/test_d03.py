import d03

def test_d03a_testdata():
    assert d03.get_mul_sum(True) == 161

def test_d03a_data():
    assert d03.get_mul_sum(False) == 174960292

def test_d03b_testdata():
    assert d03.get_mul_sum_without_donts(True) == 48

def test_d03b_data():
    assert d03.get_mul_sum_without_donts(False) == 56275602
