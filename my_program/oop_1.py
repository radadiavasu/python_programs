my_student = {
    'name': 'Vasu Radadia',
    'grades': [45, 67, 98 ,89],
    'average': None # somthing here
}

def average_grades(student):
    return sum(student['grade'] / len(student['grade']))

class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name
        self.grade = new_grade
        
    def avearge(self):
        return sum(self.grade) / len(self.grade)
    
student_one = Student('Vasu Radadia', [54, 98, 40, 54])
student_two = Student('Kunj Radadia', [63, 91, 60, 58])  

print(student_one)
print(student_two)      