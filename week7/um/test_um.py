from um import count

def test_one_um():
    assert count("Um") == 1
    assert count("um") == 1
    assert count("UM") == 1

def test_multiple_um():
    assert count("um, um, um") == 3
    assert count("Um! um, um?") == 3

def test_non_um():
    assert count("yummy, yummy") == 0
    assert count("umbrella, yummy") == 0
    assert count("Some words like yummy and yummy") == 0
