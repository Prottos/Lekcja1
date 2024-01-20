class Engineer:

    def __init__(self, name):
        self.name = name

    def build(self):
        ...

    @staticmethod                           # kiedy nie potrzebujemy "self" w metodzie
    def calculate_taxes(salary):
        return salary * 0.2
    
    def __str__(self):
        return self.name
    
patryk = Engineer("Patryk")
# print(Engineer.calculate_taxes(patryk, 6000))
print(patryk.calculate_taxes(6000))