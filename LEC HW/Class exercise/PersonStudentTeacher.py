class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
    
    def setaddress(self):
        return self.address

    def getname(self):
        return self.name
    
    def getaddress(self):
        return self.address
    
    def __str__(self): 
        return f"Name: {self.name}\n Address: {self.adress}"


class Student(Person):
    def __init__(self, name, address, numCourses, courses, grades):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades
    
    
class Teacher(Person):
    def __init__(self, name, address, numCourses, courses):
        super().__init__(name,address)
        self.numCourses = numCourses
        self.courses = courses
