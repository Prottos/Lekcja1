from src.add import add

def test_add_should_add_two_numbers():
    result = add(9, 6)
    
    assert result == 15, "Result should've been 15"
    # assert zastępuje te 2 linijki poniżej

    # if result != 15:
    #    raise AssertionError("Result should have been 15")



    # try:
    #     5 / 0
    # except ZeroDivisionError:
    #     print("nie wolno dzielić przez zero, ale nie wywalę programu")                                     # nie wywali programu
    # raise ZeroDivisionError("Niby nie podzieliłem przez zero ale i tak wywaliłem pythona")                 # stopuje proces i wywala błąd