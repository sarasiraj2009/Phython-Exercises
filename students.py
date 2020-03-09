class Student:
    def __init__(self, name, age, year, class_):
        self.name = name
        self.age = int(age)
        self.year = year
        self.class_ = class_
    def average(self, english, math, physics):
        testaverage =(english + math + physics)/3
        return testaverage



John = Student("John", 21, "2018","3")
Jane = Student("Jane", 22, "2010", "1")

print(getattr(John, "class_"))
print(John.year)
print(John.average(20,50,60))