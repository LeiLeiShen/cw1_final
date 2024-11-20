#先把抽象类写好
from CW1_Program.courses import Course
from CW1_Program.utils import *
import json
class Users():
    '''
    父类user
    此后的student，teacher，admin都继承自user
    user_id:个人身份的唯一标识，unique
    user_name:用户姓名
    user_password:用户密码
    role:用户角色，学生/老师/管理员
    '''
    def __init__(self,user_id,user_name,user_password,role):
        self.user_name=user_name
        self.user_id=user_id
        self.user_password=user_password
        self.role=role

    def display(self):
        print(f"User ID: {self.user_id}")
        print(f"Username: {self.user_name}")
        print(f"Role: {self.role}")

class Student(Users):
    def __init__(self,user_id,user_name,user_password):
        super().__init__(user_id,user_name,user_password,role='student')
        #self.enrolled_courses = []
        users_data = load_user()
        for user in users_data:
            if user['user_id'] == user_id:
                self.enrolled_courses = user.get('enrolled_courses', [])
                break
        else:
            self.enrolled_courses = []  # 如果未找到用户，初始化为空列表

    def view_available_course(self):
        #查看可选课程
        #这里在之后可以加一个key来判断能选的课
        course=load_course()
        print("all the available courses:",end='\n')
        for i in course:
            print(f"course name: {i['course_name']}, course_id: {i['course_id']}")

    def enroll_course(self):
        #加入课程
        course = load_course()
        course_id=input("please type in the course id OF the course that you want to enroll: ")

        #查找课程
        for i in course:
            if i['course_id']==course_id:
                if self.user_id not in i['student_list']:
                    i['student_list'].append(self.user_id)
                    self.enrolled_courses.append(course_id)
                    save_course(course)

                    users = load_user()
                    for j in users:
                        if j['user_id']==self.user_id:
                            j['enrolled_courses']=self.enrolled_courses
                            break
                    save_user(users)

                    print('your had successfully enrolled')
                    return
                else:
                    print('your had already enrolled')
                    return
        print('the class does not exist')

    def view_enrolled_course(self):
        #查看已经加入的课程
        if not self.enrolled_courses:
            print("you haven't enrolled any course")
        else:
            print("you have enrolled in the following course")
        for course_id in self.enrolled_courses:
            print(f"course id: {course_id}")



class Teacher(Users):
    def __init__(self,user_id,user_name,user_password):
        super().__init__(user_id,user_name,user_password,role='teacher')
        #self.course_teach = []
        users_data = load_user()
        for user in users_data:
            if user['user_id'] == user_id:
                self.course_teach = user.get('course_teach', [])
                break
        else:
            self.course_teach = []  # 如果未找到用户，初始化为空列表


    def create_course(self):
        #创建课程
        course_id = input('Enter course ID: ')
        course_name = input('Enter course name: ')

        new_course = {
            'course_id': course_id,
            'course_name': course_name,
            'teacher_id': self.user_id,
            'student_list': []
        }
        course=load_course()
        course.append(new_course)
        save_course(course)
        self.course_teach.append(course_id)
        #之后考虑要在初始化的时候就把teach这个列表写好
        user_data=load_user()
        '''
        改！！！！
        '''
        for user in user_data:
            if user['user_id']==self.user_id:
                user['course_teach']=self.course_teach
        save_user(user_data)
        print(f'the course {course_name} ,id: {course_id }has been created')


    def view_students(self):
        #查看学生
        #根据选中的课程查看课程中的学生
        if not self.course_teach:
            print("you dont have any student")
            return
        for idx,course in enumerate(self.course_teach,1):
            print(f'{idx}.course_id: {course}') #给遍历的内容加个索引
        choice=int(input('type in the serial number of the course you wanna view: '))
        '''
        这里的教师在查看学生的时候，可能因为各种原因会导致出现bug
        所以加入try except
        '''
        try:
            choice=int(choice)
            if 0<choice<len(self.course_teach)+1:
                selected_course=self.course_teach[choice-1]
                course_data=load_course()
                for course in course_data:
                    if course['course_id']==selected_course:
                        students=course['student_list']
                        if not students:
                            print('there is no student in the course')
                        else:
                            print(f'the student of class{selected_course} are followed')
                            for student in students:
                                print(student,end=',')
                        return
                print('This course may already been deleted,please refresh the program and login again')
                #删除课程后再查看可能导致当前缓存中有这个课程但实际上并没有的残留情况
            else:
                print('you type in an invalid serial number')
        except ValueError:
            print('please enter a valid serial number')




    def view_course_teach(self):
        #查看教授的课程
        if not self.course_teach:
            print("you are not teaching any class")
        else:
            print("the class you teach are list followed")
            for i in self.course_teach:
                print(f'course_id:{i}')

    def manage_student_of_course(self):
        #管理学生 增/删
        course_id = input('Enter course ID: ')
        if course_id in self.course_teach:
            course_data=load_course()
            for course in course_data:
                if course['course_id']==course_id:
                    print("the student in this course are followed")
                    print(course['student_list'])
                    manage=input('what you wanna do?(add/remove)')
                    #增
                    '''
                    这里还要修改学生的json
                    '''
                    # 根据输入决定是增加学生还是移除学生
                    if manage=='add':
                        student_id=input('enter student ID: ')
                        user_data=load_user()
                        student_exist=False
                        #用flag来判断学生是否存在
                        for user in user_data:
                            if user['user_id']==student_id and user['role']=='student':
                                student_exist = True
                                if student_id not in course['student_list']:
                                    course['student_list'].append(student_id)
                                    user['enrolled_courses'].append(course_id)
                                    print(f'you had added the student {student_id} to the course {course_id}')
                                    break
                                else:
                                    print(f'student {student_id} is already enrolled in this course')
                        if not student_exist:
                            print(f'student {student_id} is not exist')
                        save_course(course_data)
                        save_user(user_data)
                    #删
                    elif manage=='remove':
                        student_id=input('enter student ID: ')
                        user_data = load_user()
                        student_exist2 = False
                        for user in user_data:
                            if user['user_id'] == student_id and user['role'] == 'student':
                                student_exist2 = True
                                if student_id in course['student_list']:
                                    course['student_list'].remove(student_id)
                                    user['enrolled_courses'].remove(course_id)
                                    print(f'you had removed the student {student_id} from coursee {course_id}')
                                    break
                                else:
                                    print(f'student {student_id} is not enrolled in this course{course_id}')
                                    break
                        if not student_exist2:
                            print(f'student {student_id} is not exist')
                        save_course(course_data)
                        save_user(user_data)
                    else:
                        print('wrong input')
        else:
            print(f"the course {course_id} does not exist or you dont have permission to manage this course")

    def manage_course(self):
        #管理课程 改id或者名字
        course_id=input('Enter course ID: ')
        if course_id in self.course_teach:
            course_data=load_course()
            for course in course_data:
                if course['course_id']==course_id:
                    print(f'the course {course["course_id"]} ,name: {course["course_name"]}, \
                    teacher: {course["teacher_id"]}')
                    print('1.detele the course')
                    print('2.change the name of course')
                    manage=input('what you wanna do (1/2)')
                    '''
                    if manage=='1':
                        new_id=input('enter new course ID: ')
                        # 你修改了课程id的话，老师教授的课程列表中的id也得改
                        
                        #坏了，学生的enroll列表也得改，，要不把这个功能去了吧
                        
                        user_data=load_user()
                        for user in user_data:
                            if user['user_id']==course['teacher_id']:
                                user["course_teach"].remove(course['course_id'])
                        course['course_id']=new_id
                        print(f'the id of course {course["course_name"]} has benn changed to {course["course_id"]}')
                        for user in user_data:
                            if user['user_id']==course['teacher_id']:
                                user["course_teach"].append(course['course_id'])
                    '''
                    if manage=='1':
                        user_data=load_user()
                        for user in user_data:
                            if user['role'] == 'student':
                                if course_id in user.get('enrolled_courses', []):
                                    user['enrolled_courses'].remove(course_id)#由于删除了课程，所以把学生上课列表中的这门课也删了
                            # 处理教师用户
                            elif user['role'] == 'teacher':
                                if course_id in user.get('course_teach', []):
                                    user['course_teach'].remove(course_id)

                        course_data.remove(course)
                        save_course(course_data)
                        save_user(user_data)
                    elif manage=='2':
                        new_name=input('enter new course name:')
                        course['course_name']=new_name
                        print(f'the name of course {course["course_id"]} has benn changed to {course["course_name"]}')
                    else:
                        print("wrong input")

                    save_course(course_data)
                    return
        else:
            print(f"the course {course_id} does not exist or you dont have permission to manage this course")

