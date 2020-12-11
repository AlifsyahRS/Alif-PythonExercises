class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.getName()}({self.getAddress()})"

    def getName(self):
        return str(self.name)

    def getAddress(self):
        return str(self.address)

    def setAddress(self, new_address):
        self.address = new_address


class Teacher(Person):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        Person.__init__(self, self.name, self.address)
        self.course = []

    def __str__(self):
        return f"Teacher: {super().__str__()}"

    def addCourse(self, new_course):
        if new_course not in self.course:
            self.course.append(new_course)
            return True
        else:
            return False

    def removeCourse(self, del_course):
        if del_course in self.course:
            self.course.remove(del_course)
            return True
        else:
            return False

    def courseInquiry(self):
        statement = f"Courses that {self.name} teaches:"
        for i in self.course:
            statement += f" {i},"
        return statement.rstrip(',')


class Student(Person):
    def __init__(self, name, address):
        self.name = name
        self.address = address
        Person.__init__(self, self.name, self.address)
        self.courses = {}
        self.num_courses = len(self.courses)

    def __str__(self):
        return f"Student: {super().__str__()}"

    def addCourseGrade(self, course, grade):
        if course not in self.courses:
            self.courses[course] = [grade]
        else:
            self.courses[course].append(grade)

    def printGrades(self):
        for i in self.courses:
            print(f"{self.name}'s grades for {i}:")
            for j in self.courses[i]:
                print(j)

    def getAverageGrades(self):
        total = 0
        counter = 0
        for i in self.courses:
            for j in self.courses[i]:
                total += j
                counter += 1
        average = total / counter
        return f"Grades Average: {average}"

    def courseInquiry(self):
        statement = f"Courses that {self.name} takes:"
        for i in self.courses:
            statement += f" {i},"
        return statement.rstrip(',')
