from datetime import datetime as dt

today = dt.now()
print(today)

# print(type(today))
# today = str(today)

# print("Logi_" + today[11:13] + today[14:16]+ today[17:19] + ".txt")

ts1 = today.strftime("Moja zmiena to: %H%M%S")
print(ts1)