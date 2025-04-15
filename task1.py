class Student:
    def __init__(self, name, age, height, grade):
        self.name = name
        self.age = age
        self.height = height
        self.grade = grade

    def study(self):
        print(f"{self.name} is studying hard 📚")

# Inherited Class
class CollegeStudent(Student):
    pass

# Creating an object from the base class
student1 = Student("Amina", 17, 5.3, "Grade 11")
print(student1.name)
student1.study()

# Creating an object from the inherited class
student2 = CollegeStudent("Michael", 21, 5.9, "Year 2")
print(student2.name)
student2.study()
