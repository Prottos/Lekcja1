import pytest
from src.transactions import process_transactions

def test_process_transactions():
    result = process_transactions([{"amount": 5, "type": "credit"}])
    assert result == 5

def test_empty_list():
#     """ Test negatywny (ale tak jak niżej się go nie pisze - wersja prymitywna)
#     Jeżeli wyjątek wystąpi: PASS
#     Jeżeli wyjątek nie wystąpi: FAIL
#     """
#     try:
#         result = process_transactions([])
#     except ValueError:
#         print("Pass")
#         # Złapałem pustą listę transakcji
#     else:
#         raise AssertionError("When providing empty list, ValueError should've been raised")
#         # Kod w sekcji "try" nie wyrzucił żadnego wyjątku
#     # finally:
#     #    ...
#         # kod wykonuje się zawsze
    with pytest.raises(ValueError, match="list is empty."):   # krótsze, czytelniejsze
        process_transactions([])
def test_is_dict():
    with pytest.raises(ValueError):
        process_transactions([5])

def test_valid_dict():
    with pytest.raises(ValueError):
        process_transactions([{"haba":"baba"}])

def test_invalid_format():
    with pytest.raises(ValueError):
        process_transactions([{"type": 5, "amount":5}])

def test_invalid_amount():
    with pytest.raises(ValueError):
        process_transactions([{"type": "credit", "amount": "5"}])

def test_transfer_negative_value():
    with pytest.raises(ValueError):
        process_transactions([{"type": "credit", "amount": -5}])