from datetime import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f"My name is {self.name}. I'm {self.age} years old.")
    def birthyear(self):
        birthyear = datetime.now().year - self.age
        print(f"I was born on {birthyear}.")

class Student(Person):
    def __init__(self, name, age, school, gradyear):
        super().__init__(name, age)
        self.school = school
        self.gradyear = gradyear
    def graduation(self):
        year = self.gradyear - datetime.now().year
        gradage = year + self.age
        if year > 0:
            print(f"I will graduate from {self.school} in {year} years. I will be {gradage} by then.")
        elif year == 0:
            print(f"I will graduate from {self.school} this year.")
        else:
            year = abs(year)
            print(f"I graduated from {self.school} {year} years ago when I was {gradage}.")
    


p1 = Person("Josh", 34)
p1.introduce()
p1.birthyear()

s1 = Student("Jamie", 20, "Asia Pacific College", 2026)
s1.introduce()
s1.graduation()

