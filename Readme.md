
# Course Management System

## Introduction

The **Course Management System** is a program implemented in Python. It supports three user roles:
- **Student**
- **Teacher**
- **Administrator**

This system provides comprehensive course management functions.

### System Structure:

```
--data
   |-- user.json
   |-- courses.json
-- admin.py
-- courses.py
-- main.py
-- user.py
-- utils.py
-- readme.md
```

### Requirements:

- **Python Version**: 3.9
- **Dependencies**: None (No external libraries required)
- Ensure the following:
  - `user.json` and `courses.json` are in the `data` folder.
  - Other files and the `data` folder are in the same directory.

#### Example User Data in `user.json`:
```json
{
  "user_id": "S001",
  "user_name": "student1",
  "user_password": "password123",
  "role": "student",
  "enrolled_courses": ["C001", "C002", "C003"]
}
```

---

## Operating Instructions

1. **Run the Program**:
   - Navigate to the project root in the terminal.
   - Execute the following command:
     ```bash
     python main.py
     ```
2. **Login**:
   - Enter the user ID and password when prompted to log in.
   - Start using the system.

### Sample User Credentials:

| Role       | User ID | Password      |
|------------|---------|---------------|
| Student    | S001    | password123   |
| Teacher    | T001    | password456   |
| Administrator | A001 | adminpass     |

---

## Author Information

- **Name**: Lei SHEN
- **Student ID**: 20717323
- **Email**: [scxls3@nottingham.edu.cn](mailto:scxls3@nottingham.edu.cn)
