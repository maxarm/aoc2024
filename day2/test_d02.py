import d02

def test_d02a_testdata():
    assert d02.get_number_of_safe_reports(False, True) == 2

def test_d02a_data():
    assert d02.get_number_of_safe_reports(False, False) == 390

def test_d02b_testdata():
    assert d02.get_number_of_safe_reports(True, True) == 5

def test_d02b_data():
    assert d02.get_number_of_safe_reports(True, False) == 439