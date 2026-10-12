# Week 2 — Classes, objects, constructors, inheritance, polymorphism

class Person:
    school = "NAVTTC AI/ML Practice"  # class variable

    def __init__(self, name):
        self.name = name  # instance variable

    def introduce(self):
        return f"My name is {self.name}."

class Student(Person):
    def __init__(self, name, course):
        super().__init__(name)
        self.course = course

    def introduce(self):  # overriding = polymorphism
        return f"My name is {self.name}; I am studying {self.course}."

people = [Person("Ali"), Student("Ayesha", "Python")]
for person in people:
    print(person.introduce())

print("Class variable:", Person.school)
