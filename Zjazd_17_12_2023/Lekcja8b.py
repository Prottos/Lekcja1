class Person:
    def __init__ (self, name, age, id=0):                       # metody magiczne to te z "__" z przodu i tyłu
        # self.name = "Patryk"
        self.name = name
        # self.age = 26
        self.age = age
        self.id = id
    def hello(self):
        # print("Cześć, jestem " + self.name + " i mam " + str(self.age) + " lat", end="\n\n")
        # print("Cześć, jestem", self.name, "i mam", self.age, "lat", end="\n\n")
        print(f"Cześć, jestem {self.name} i mam {self.age} lat. Moje ID to: {self.id}", end="\n\n")

    def __str__(self):
        return f"Obiekt z klasy Person o nazwie: {self.name}, wieku: {self.age} lat, ID: {self.id}"
    
    def __del__ (self):
        print("Ubili mnie")
# class Something(Person):        # dziedziczenie po klasie, można używać def'ów z dziedziczonego obiektu
#     def Process1(self):
#         return 3
#     def Process2(self):
#         print(2)

# patryk = []

# for i in range(10):
#     patryk2 = Person("Patryk", 26, i)
#     patryk.append(patryk2)

# for ppl in patryk:
#     ppl.hello()
        
patryk = Person("Patryk", 26)
# patryk.hello()

print(patryk)                   # <__main__.Person object at 0x0000024D21E0FD50> <- w programie main jest obiekt klasy Person w lokalizacji 0x00...

del patryk