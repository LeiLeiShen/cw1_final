# main.py

import json

from CW1_Program.users import Student, Teacher
from CW1_Program.admin import Admin
from CW1_Program.utils import *




def login():
    users_data = load_user()
    user_id = input("please enter your id: ")
    user_password = input("please enter your password: ")

    for user in users_data:
        if user['user_id'] == user_id and user['user_password'] == user_password:
            role = user['role']
            user_name = user['user_name']
            # 根据角色实例化相应的用户对象
            if role == 'student':
                student = Student(user_id, user_name, user_password)
                student.enrolled_courses = user.get('enrolled_courses', [])
                return student
            elif role == 'teacher':
                teacher = Teacher(user_id, user_name, user_password)
                teacher.courses_teaching = user.get('courses_teaching', [])
                return teacher
            elif role == 'admin':
                admin = Admin(user_id, user_name, user_password)
                return admin
    print("wrong id or password")
    return None

def student_menu(student):
    while True:
        print("\nStudent Menu")
        print("1.view_available_course")
        print("2.enroll_course")
        print("3.view_enrolled_course")
        print("4.search")
        print("5.exit")
        choice = input("please enter your choice: ")
        if choice == '1':
            student.view_available_course()
        elif choice == '2':
            student.enroll_course()
        elif choice == '3':
            student.view_enrolled_course()
        elif choice == '4':
            search_info=input("please enter the course info(id/name) that you wanna search")
            course_list=search(search_info)
            print('the course that you search may list followed')
            if course_list :
                for course in course_list:
                    print(f'name: {course["course_name"]},id: {course["course_id"]}')
            else:
                print('no courses found')
        elif choice == '5':
            break
        else:
            print("invalid choice")

def teacher_menu(teacher):
    while True:
        print("\nTeacher Menu")
        print("1.create_course")
        print("2.view_students")
        print("3.view_course_teach")
        print("4.manage_student_of_course")
        print("5.manage_course")
        print("6.search")
        print("7.exit")
        choice = input("please enter your choice: ")
        if choice == '1':
            teacher.create_course()
        elif choice == '2':
            teacher.view_students()
        elif choice == '3':
            teacher.view_course_teach()
        elif choice == '4':
            teacher.manage_student_of_course()
        elif choice == '5':
            teacher.manage_course()
        elif choice == '6':
            search_info=input("please enter the course info(id/name) that you wanna search")
            course_list=search(search_info)
            print('the course that you search may list followed')
            if course_list :
                for course in course_list:
                    print(f'name: {course["course_name"]},id: {course["course_id"]}')
            else:
                print('no courses found')
        elif choice == '7':
            break
        else:
            print("invalid choice")
def admin_menu(admin):
    while True:
        print("\nAdmin Menu")
        print("1.add_user")
        print("2.delete_user")
        print("3.view_all_users")
        print("4.add_course")
        print("5.delete_course")
        print("6.edit_course")
        print("7.view_courses")
        print("8.search")
        print("9.exit")
        choice = input("please enter your choice: ")
        if choice == '1':
            admin.add_user()
        elif choice == '2':
            admin.delete_user()
        elif choice == '3':
            admin.view_all_users()
        elif choice == '4':
            admin.add_course()
        elif choice == '5':
            admin.delete_course()
        elif choice == '6':
            admin.edit_course()
        elif choice == '7':
            admin.view_courses()
        elif choice == '8':
            search_info=input("please enter the course info(id/name) that you wanna search")
            course_list=search(search_info)
            print('the course that you search may list followed')
            if course_list :
                for course in course_list:
                    print(f'name: {course["course_name"]},id: {course["course_id"]}')
            else:
                print('no courses found')
        elif choice == '9':
            break
        else:
            print("invalid choice")


def main():
    while True:
        print("welcome to LeiShen's Course Management System")
        print("1.Login")
        print("2.Exit")
        choice = input("enter the choice")
        if choice == '1':
            user = login()
            if user:
                if user.role == 'student':
                    student_menu(user)
                elif user.role == 'teacher':
                    teacher_menu(user)
                elif user.role == 'admin':
                    admin_menu(user)
        elif choice == '2':
            print("have a good day!bye bye")
            break
        else:
            print("invalid choice")

if __name__ == '__main__':
    main()