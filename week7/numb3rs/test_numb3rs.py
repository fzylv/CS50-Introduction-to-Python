from numb3rs import validate

def test_valid():
    assert validate("192.168.1.1") == True
    assert validate("8.8.8.8") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_invalid():
    assert validate("275.3.6.28") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.4.5") == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("1234.1.1.1") == False

def test_edge_cases():
    assert validate("0.0.0.00") == True

