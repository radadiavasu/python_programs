# For loop
students = [
    {"Name": "Vasu", "Grade": 45}, 
    {"Name": "Parth", "Grade": 65},
    {"Name": "Kunj", "Grade": 34},
    {"Name": "Jay", "Grade": 24}
]
for student in students:
    Name = student["Name"]
    Grade = student["Grade"]
    print(f"{Name} has the grade of {Grade}")