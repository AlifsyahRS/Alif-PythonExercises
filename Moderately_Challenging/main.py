from Person import Teacher, Student

student_alif = Student("Alif", "Jakarta")  # I ain't revealing my address lol
teacher_jude = Teacher("Jude", "Jakarta")


def student():
    print(student_alif.__str__())
    student_alif.addCourseGrade("ITP", 100)
    student_alif.addCourseGrade("ITP", 87)
    student_alif.addCourseGrade("Multimedia and HCI", 98)
    print(student_alif.courseInquiry())
    student_alif.printGrades()
    print(student_alif.getAverageGrades())


def teacher():
    teacher_jude.__str__()
    teacher_jude.addCourse("ITP")
    teacher_jude.addCourse("ITP")
    teacher_jude.addCourse("Multimedia and HCI")
    teacher_jude.removeCourse("Multimedia and HCI")
    print(teacher_jude.courseInquiry())


def main():
    student()
    teacher()


if __name__ == "__main__":
    main()
