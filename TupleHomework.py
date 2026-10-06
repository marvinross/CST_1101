Tuple_Marcus = ("Marcus", 86, 92, 97, 82, 89)
Tuple_Tiffany = ("Tiffany", 98, 95, 88, 91, 93)
Tuple_Jimmy = ("Jimmy", 73, 78, 83, 85, 71)
Tuple_Robert = ("Robert", 97, 98, 100, 98, 100)
Tuple_Lisa = ("Lisa", 96, 100, 98, 98, 97)
Tuple_Greg = ("Greg", 68, 72, 63, 57, 66)

Student_Grades = locals()
print(Student_Grades)

Student_Average = sum(Student_Grades) / len(Student_Grades)
print(Student_Average)
