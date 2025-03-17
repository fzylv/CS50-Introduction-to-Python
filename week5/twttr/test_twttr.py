from twttr import shorten


def test_no_vowels():
    assert shorten("xyz") == "xyz"


def test_uppercase():
    assert shorten("HELLO") == "HLL"
    assert shorten("TWITTER") == "TWTTR"


def test_vowels():
    assert shorten("ieu") == ""
    assert shorten("ai") == ""


def test_numbers():
    assert shorten("123") == "123"
    assert shorten("h3ll0") == "h3ll0"


def test_punctuation():
    assert shorten("hello, world!") == "hll, wrld!"
    assert shorten("cs50!") == "cs50!"


def test_mixed():
    assert shorten("Hello, World 123!") == "Hll, Wrld 123!"
