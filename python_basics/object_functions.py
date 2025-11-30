# Class with object functions (methods)

class Student:
    def __init__(self, name, major, cgpa):
        self.name = name
        self.major = major
        self.cgpa = cgpa

    def on_honor_roll(self):
        return self.cgpa >= 8.0


student1 = Student("Shivi", "CSE", 8.7)
student2 = Student("John", "IT", 7.2)

print(student1.on_honor_roll())   # True
print(student2.on_honor_roll())   # False