import d02

def test_d02a_testdata():
    assert d02.get_number_of_safe_reports(True) == 2

def test_d02a_data():
    assert d02.get_number_of_safe_reports(False) == 390