import json
import os
import re
'''
工具类
用来加载文件
'''
def load_user():
    if os.path.exists('data/users.json'):
        with open('data/users.json','r')as filename:
            return json.load(filename)
    else:
        return []

def save_user(user_data):
    with open('data/users.json','w')as filename:
        json.dump(user_data,filename)

def load_course():
    if os.path.exists('data/courses.json'):
        with open('data/courses.json','r')as filename:
            return json.load(filename)
    else:
        return []

def save_course(course_data):
    with open('data/courses.json','w')as filename:
        json.dump(course_data,filename)

#直接把搜索写在工具类里，各个角色都能调用
'''
def search(course_info):
    courses_info_lower = course_info.lower()
    courses_data=load_course()
    maching_course=[]
    for course in courses_data:
        if courses_info_lower in course['course_name'].lower():
            maching_course.append(course)
        elif courses_info_lower == course['course_id'].lower():
            maching_course.append(course)
    return maching_course
'''




def search(course_info):
    course_info_lower = course_info.lower()
    courses_data = load_course()
    matching_courses = []

    for course in courses_data:
        if re.search(course_info_lower, course['course_name'].lower()) or \
                course_info_lower == course['course_id'].lower():
            matching_courses.append(course)

    return matching_courses
