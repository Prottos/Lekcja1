from src.even_or_odd import is_even

def test_even():
    result = is_even(8)
    result2 = is_even(7)
    assert result is True and result2 is False