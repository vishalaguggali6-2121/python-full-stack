student_courses={
    "Asha":"python",
    "Ravi":"Data Analytics",
    "Neha":"AI"
    }
print("Student names:",list(student_courses.keys()))
print("enrolled courses:",list(student_courses.values()))
name=input("enter student name to check:")
print(f"{name}exists:",name in student_courses)
