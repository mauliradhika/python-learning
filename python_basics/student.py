from classes_objects import Student, Book

student1 = Student("Jim", "Business", 8.9, False)
student2 = Student("Pam", "Art", 9.5, True)

print(student1.name) # Jim
print(student2.cgpa) # 9.5

book1 = Book("Atomic Habits", "James Clear", 280)
book2 = Book("1984", "George Orwell", 328)

print(book1.short_info())
print(book2.short_info())