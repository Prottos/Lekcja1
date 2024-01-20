import sys
from rate import get_rate

def main():
    rate = get_rate(sys.argv[1])
    print(rate)