from CW1_Program.courses import Course
from CW1_Program.utils import *
import json
from CW1_Program.users import Users


class Admin(Users):
    '''
    因为user类内容太多了所以新开一个文件存admin、
    add_user 添加用户
    delete_user 删除用户
    view_all_users 查看所有用户
    add_course 添加课程
    delete_course 删除课程
    edit_course 编辑课程信息
    view_courses 查看所有课程
    '''
    def __init__(self, user_id, user_name, user_password):
        super().__init__(user_id, user_name, user_password, role='admin')

    def add_user(self):
        user_id = input("please enter new users' id : ")
        user_name = input("please enter new users' name : ")
        user_password = input("please enter new users' password: ")
        role = input("please enter new users' role(student/teacher/admin): ")
        if role not in ['student', 'teacher', 'admin']:
            print('invalid role')
            return

        users_data=load_user()
        #检查一下是否已经存在同样的用户id
        for user in users_data:
            if user['user_id'] == user_id:
                print('user already exists')
                return

        new_user ={
            'user_id': user_id,
            'user_name': user_name,
            'user_password':user_password,
            'role':role
        }
        if role == 'student':
            new_user['enrolled_courses'] = []
        elif role == 'teacher':
            new_user['course_teach'] = []

        users_data.append(new_user)
        save_user(users_data)
        print(f'new user {user_id} was successfully added')

    def delete_user(self):
        user_id = input("please enter the user's id to delete :")
        users_data = load_user()
        for user in users_data:
            if user['user_id'] == user_id:
                users_data.remove(user)
                save_user(users_data)
                print(f"the {user_id} was successfully deleted")
                return
        print("can not find this user")

    def view_all_users(self):
        users_data = load_user()
        print("followed by are all users in the system")
        for user in users_data:
            print(f'the user {user["user_name"]}, the id is {user["user_id"]},role is {user["role"]}')

    def add_course(self):
        # 创建课程
        course_id = input('Enter course ID: ')
        course_name = input('Enter course name: ')
        teacher_id = input('Enter teacher ID: ')
        #这里有空得写个检查，教师和课程的合法性

        course_data = load_course()
        user_data=load_user()
        teacher_exist=False
        for user in user_data:
            if user['user_id'] == teacher_id and user['role']=='teacher':
                teacher_exist=True
                break
        if not teacher_exist:
            print(f'the teacher {teacher_id} does not exist')
            return

        for course in course_data:
            if course['course_id'] == course_id:
                print(f'the course {course_id} is already exist')
                return

        new_course = {
            'course_id': course_id,
            'course_name': course_name,
            'teacher_id': teacher_id,
            'student_list': []
        }
        for user in user_data:
            if user['user_id'] == teacher_id and user['role']=='teacher':
                user['course_teach'].append(course_id)
        course_data.append(new_course)
        save_course(course_data)
        save_user(user_data)
        print(f"the course {course_id} was successfully added ")

    def delete_course(self):
        course_id =input('please enter the course id: ')
        course_data=load_course()
        user_data = load_user()
        for course in course_data:
            if course['course_id']==course_id:

                for user in user_data:
                    if user['role'] == 'student':
                        if course_id in user.get('enrolled_courses', []):
                            user['enrolled_courses'].remove(course_id)
                    # 处理教师用户
                    elif user['role'] == 'teacher':
                        if course_id in user.get('course_teach', []):
                            user['course_teach'].remove(course_id)

                course_data.remove(course)
                save_course(course_data)
                save_user(user_data)
                print(f"the course {course_id} was successfully deleted")
                return
        print(f'can not find the course {course_id}')

    def edit_course(self):
        course_id = input('Enter course ID: ')
        course_data = load_course()
        for course in course_data:
            if course['course_id'] == course_id:
                print(f'the course {course["course_id"]} ,name: {course["course_name"]}, \
                        teacher: {course["teacher_id"]}')
                #print('1.change the id of course')
                print('2.change the name of course')
                print('3.change the teacher of this course')
                manage = input('what you wanna do (2/3)')
                '''
                if manage == '1':
                    new_id = input('enter new course ID: ')
                    course['course_id'] = new_id
                    print(f'the id of course {course["course_name"]} has benn changed to {course["course_id"]}')
                '''
                if manage == '2':
                    new_name = input('enter new course name:')
                    course['course_name'] = new_name
                    print(
                        f'the name of course {course["course_id"]} has benn changed to {course["course_name"]}')
                elif manage == '3':
                    new_teacher_id = input('enter new teacher id: ')
                    user_data=load_user()
                    teacher_exist=False
                    for teacher in user_data:
                        if teacher['user_id'] == new_teacher_id and teacher['role'] == 'teacher':
                            teacher_exist=True
                            break
                    if not teacher_exist:
                        print(f'teacher {new_teacher_id} is not exist')
                        return
                    for user in user_data:
                        if user['role']=='teacher':
                            if course_id in user['course_teach']:
                                user['course_teach'].remove(course_id)
                    course['teacher_id'] = new_teacher_id
                    for user in user_data:
                        if user['role'] == 'teacher':
                            if user['user_id'] == new_teacher_id:
                                user['course_teach'].append(course_id)
                    print('the teacher of course is updated')
                    save_course(course_data)
                    save_user(user_data)
                else:
                    print("wrong input")
                save_course(course_data)

                return

        print(f'can not find the course {course_id}')

    def view_courses(self):
        course_data=load_course()
        print('all the course in system are listed followed')
        for course in course_data:
            print(f'course_id: {course["course_id"]}, course_name: {course["course_name"]},\
                  teacher:{course["teacher_id"]}')

