# Student Learning Portal

**Course:** PROG211 — Object-Oriented Programming 1  
**Project domain:** Education  
**Language:** Python 3

## 1. Overview
The Student Learning Portal is a small console application for adding students, viewing their course and progress information, and updating progress. It uses fictional sample records and does not ask for sensitive personal data.

## 2. How to run
1. Install Python 3.
2. Download `student_portal.py`.
3. Open a terminal or command prompt in the folder containing the file.
4. Run:

```bash
python student_portal.py
```

If your computer uses `python3`, run `python3 student_portal.py`.

## 3. Example use
The program starts with two fictional sample students. Choose option `2` to view the records. Choose `3`, enter `ST001`, and set progress to `In progress` or `Completed`. Choose `1` to add another student, or `4` to exit.

Example output (the exact display depends on the user's choices):

```text
Student added successfully.
Student added successfully.

Welcome to the Student Learning Portal
1. Add student
2. View all students
3. Update student progress
4. Exit

Choose an option (1-4): 2

--- Student Records ---
ID: ST001 | Name: Aminata Kamara | Course: Introduction to Python | Progress: Not started
ID: ST002 | Name: Joseph Conteh | Course: Database Basics | Progress: Not started
Total Student objects created: 2
```

## 4. OOP concepts used
- **Classes:** `Student` and `LearningPortal`.
- **Objects:** each student record is a `Student` object; `portal` is a `LearningPortal` object.
- **Attributes:** `student_id`, `name`, `course`, and `progress` describe each student.
- **Instance methods:** `display_info()` and `update_progress()` work with a particular student object.
- **Class attribute:** `total_students` is shared by the `Student` class.
- **Class method:** `create_demo_student()` is marked with `@classmethod` and creates a student using `cls`.
- **Object interaction:** the portal stores and calls methods on Student objects.

## 5. Data structure
The program uses one required data structure: a **list**, `self.students`, to store multiple Student objects. It loops through the list to display records and find a student by ID.

## 6. Digital Public Goods (DPG) alignment
- **Open-source:** the source code can be published in a public GitHub repository with a suitable open-source licence chosen by the student/instructor.
- **Inclusive and accessible design:** the application uses a simple text menu, clear prompts, and plain-language error messages.
- **Privacy-respecting:** the demonstration uses fictional data and does not collect passwords, contact details, grades, or other sensitive personal data. This is a classroom demonstration, not a production student database.
- **Modular and reusable:** student information and behaviour are kept in the `Student` class, while record management is handled by `LearningPortal`.

These are design intentions for this small assignment; a production system would need further security, accessibility, and data-protection review.

## 7. Testing checklist
- [ ] View the two sample students.
- [ ] Add a student with a new ID.
- [ ] Try adding a duplicate ID.
- [ ] Update a known student's progress.
- [ ] Enter an invalid progress value.
- [ ] Search for an unknown student ID.
- [ ] Exit the program.

## 8. Suggested GitHub submission
Create a repository named `student-learning-portal`. Upload `student_portal.py` and this `README.md`. Add your lecturer as a repository collaborator using the GitHub repository settings. Include screenshots of a successful run in your printed submission.
