# jak pobrać aktualny kurs waluty?
import httpx
import json

def get_rate(currency: str) -> float:
    response = httpx.get(f'https://api.nbp.pl/api/exchangerates/rates/a/{currency.lower()}/last/1/?format=json')
    response_as_dict = response.json()
    return float(response_as_dict["rates"][0]["mid"])

# def show_rate(code):
#    code = input("Wprowadź kod waluty: ")
    # rate = get_rate(f"{code.upper()}")
    # print(f"Kurs {code.upper()} wynosi {rate}zł")