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
     
    def toString(self):
        return f"name: {self.name}\nAddress: {self.address}\nNumber of Courses: {self.numCourses}\nCourses: {self.courses}\nGrades: {self.grades}"
    
    def addCoursesGrade(self, course, grade):
        self.courses.append(course)
        self.grades.append(grade)
        self.numCourses+= 1

    def printGrades(self):
        print(f"Here are the grades of {self.name}: \n")
        for i in range(self.numCourses):
            print(f"{self.courses[i]}: {self.grades[i]} \n")

    def getAverageGrades(self):
        total= 0
        for grade in self.grades:
            total+=grade
        return total/self.numCourses

class Teacher(Person):
    def __init__(self, name, address, numCourses = 0, courses = []):
        super().__init__(name,address)
        self.numCourses = numCourses
        self.courses = courses
    
    def addCourse(self, course):
        if course in self.courses:
            print("Course already exists")
            return False
        else:
            self.courses.append(course)
            self.numCourses+=1
            return True

    def removeCourse(self, course):
        if course not in self.courses:
            print("Course does not exist")
            return False
        else:
            self.courses.remove(course)
            self.numCourses-=1
            return True

    def toString(self):
        return f"Name: {self.name}\nAddress: {self.address}\nNumber of Courses: {self.numCourses}\nCourses: {self.courses}"

student1= Student("Tiffany","Apt K Place")
student1.addCoursesGrade("Scientific Computing",100)
student1.addCoursesGrade("Discrete Mathematics", 93)
print(student1.toString())
student1.printGrades()
print(f"Average Grades: {student1.getAverageGrades}")
