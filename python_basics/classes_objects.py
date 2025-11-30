class Student:

    def __init__(self, name, major, cgpa, is_on_probation):
        self.name = name
        self.major = major
        self.cgpa = cgpa
        self.is_on_probation = is_on_probation

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def short_info(self):
        return f"{self.title} by {self.author}"