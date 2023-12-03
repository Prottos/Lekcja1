import argparse

parser = argparse.ArgumentParser()
parser.add_argument("filename")             # dodaj argumenty
# parser.add_argument("mode")
parser.add_argument("-m",                   # arguemnt z jednym "-" to zwyczajowo nazwa skrócona, a "--" to nazwa argumentu 
                    "--mode",               # teraz przy wpisywaniu w terminalu używamy "-m", a program użyje tego jako "mode"
                    required=False)         # teraz argument jest opcjonalny przy wpisaniu
parser.add_argument("-cl", "--conflevel", type=int, default=3, required=False) # argument "conflevel", jest typem "integer", jest opcjonalny, a jeśli nie wpiszemy do domyślnie wynosi 3


args = parser.parse_args()                  # przechwyć/zczytaj argumenty

print("Nazwa pliku to ",args.filename)      # wykonuje program i wyświetla nazwę pliku podaną jako arguemnt przy uruchamianiu programu
print("Tryb pliku to ",args.mode)
print(args.conflevel)