from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello, world!") == 0
    assert value("HELLO") == 0

def test_h():
    assert value("hi") == 20
    assert value("Hi there!") == 20
    assert value("HI") == 20

def test_other():
    assert value("good morning") == 100
    assert value("What's up?") == 100
    assert value("123") == 100
    assert value("") == 100

