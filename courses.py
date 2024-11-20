
class Course:
    def __init__(self,course_id,course_name,teacher_id):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher_id = teacher_id
        self.student_list = []   #用来存这门课的学生

    def add_student(self,student_id):
        if student_id not in self.student_list:
            self.student_list.append(student_id)
            print(f'Student {student_id} has been added to the course {self.course_name}')
        else:
            print(f'Student {student_id} were already enrolled in the course {self.course_name} before')


    def remove_student(self,student_id):
        if student_id in self.student_list:
            self.student_list.remove(student_id)
            print(f'Student {student_id} has been removed from the course {self.course_name}')
        else:
            print(f'Student {student_id} was not enrolled in the course {self.course_name}')