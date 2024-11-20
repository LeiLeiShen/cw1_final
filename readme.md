Course Management System

introduction

The Course Management System is a program implemented in Python, there three user roles (student, teacher, administrator), and system provides course management functions. 

the structure of system is followed:

--data
----user.json
----courses.json

--admin.py

--courses.py

--main.py

--user.py

--utils.py

--readme.md

run requirement:
python 3.9 

there is no external dependence

please make sure that the users.json and courses.json are in the folder data
other file and data folder should in the same folder too

ep.info in json
{"user_id": "S001", "user_name": "student1", "user_password": "password123", "role": "student", "enrolled_courses": ["C001", "C002", "C003"]}

operating steps\
You can run main.py directly in the compiler

1.Navigate to the project root in the terminal\
2.run python main.py\
3.Enter the user ID and password as prompted to log in and start using the system.

some user's id and password are list followed for login\
1.id:S001  password:password123  role:student\
2.id:T001  password:password456  role:teacher\
3.id:A001  password:adminpass    role:admin


student_information
Lei SHEN
20717323
scxls3@nottingham.edu.cn