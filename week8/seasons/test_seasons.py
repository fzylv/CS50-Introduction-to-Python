from seasons import check_birthday
import pytest
from datetime import date

def test_valid():
    assert check_birthday("2000-01-01") == ("2000", "01", "01")
    assert check_birthday("1999-12-31") == ("1999", "12", "31")
    assert check_birthday("2024-02-29") == ("2024", "02", "29")

def test_invalid_format():
    with pytest.raises(ValueError):
        check_birthday("01-01-2000")
    with pytest.raises(ValueError):
        check_birthday("2000/01/01")
    with pytest.raises(ValueError):
        check_birthday("20000101")
    with pytest.raises(ValueError):
        check_birthday("abcd-ef-gh")

def test_invalid():
    with pytest.raises(ValueError):
        check_birthday("2023-02-30")
    with pytest.raises(ValueError):
        check_birthday("2021-04-31")
 


