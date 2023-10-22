# pętla for - wykona się tyle razy, ile powiemy

# for i in range(10):                 # pętla od 0 do 9 włącznie (zaczyna się od 0)
#     print(i)                        # będzie wyświatlało kolejne wartości dla 'i'

sample_list = [1,5,7,12,53,32,84,10]

#for i in range(8):                    # pętla od 0 do 7 - teraz jest wpisane na sztywno dla 8 wartości
# for i in range(len(sample_list)):      # teraz pętla wykona działanie dla tylu elementów, ile jest w liście
#     print(sample_list[i])              # wypisuje kolejno wartości ze zbióru danych 

# for i in range(3,10):                     # pętla od 3 do 9 ('i' zacznie się od 3)
# for i in range(4,15,3):                   # pętla od 4 do 15 co 3 krok
for i in range(8,2,-3):                 # pętla będzie szła w dół od 50 do 17 co 3 krok
    print(i, end=' ')                   # end sprawia, że zmienia się separator - zamiast entera (nowej linii możemy dać np. spację)