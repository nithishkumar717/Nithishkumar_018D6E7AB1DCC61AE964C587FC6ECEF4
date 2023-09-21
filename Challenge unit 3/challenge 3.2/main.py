class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
   
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students
students = [

    Student("peter", "212203767", 2.75),
    Student("tonnystark", "212203768", 3.5),
    Student("Mj", "212203769", 3.3),
    Student("eddy", "212203770", 3.9),
]

sorted_students = sort_students(students)


for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")
