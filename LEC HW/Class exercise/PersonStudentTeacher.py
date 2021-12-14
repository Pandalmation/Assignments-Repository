class Person:
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address

    def setaddress(self, address: str) -> None:
        self.address = address
    
    def setname(self, name):
        self.name = name
    
    def getname(self) -> str:
        return self.name

    def getaddress(self) -> str:
        return self.address
    
    def toString(self) -> str:
          return f"Name: {self.name}\n Address: {self.address}"

    
class Student(Person):
    def __init__(self, name, address, numCourses: int = 0, courses: str = [], grades: int = []):
        super().__init__(name, address)
        self.numCourses = numCourses
        self.courses = courses
        self.grades = grades
    
class Teacher(Person):
    def __init__(self, name, address, numCourses, courses):
        super().__init__(name,address)
        self.numCourses = numCourses
        self.courses = courses
