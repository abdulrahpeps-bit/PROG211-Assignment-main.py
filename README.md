# PROG211: Object-Oriented Programming 1 Assignment
* **University:** Limkokwing University of Creative Technology
* **Department:** Information and Communication Technology[cite: 1]
* **Module:** PROG211 (Semester 03)[cite: 1]
* **Domain:** Education (Student Learning & Results Management System)[cite: 1]

## Project Overview
This Python program utilizes Object-Oriented Programming (OOP) concepts from Lectures 1-3 to build a real-world Student Learning and Record Management System[cite: 1]. 

### Key Features Implemented:
* **Task 1 (OOP Basics):** Two distinct classes (`Student` and `StudentPortal`) with relevant attributes and interaction methods[cite: 1, 2].
* **Task 2 (Data Structures):** Uses a Python dictionary (`self.records`) to store multiple `Student` objects using their unique ID as keys, complete with add and display functions[cite: 2].
* **Task 3 (Methods & DPG Standards):** Includes instance methods for modifying records and a class method (`@classmethod`) for system metadata[cite: 2].

## Digital Public Goods (DPG) Alignment
1. **Open-Source:** Hosted publicly on GitHub for academic review and community reuse[cite: 1].
2. **Inclusive and Accessible:** Written in clean, readable Python code adhering to standard formatting and clear comments.
3. **Privacy-Respecting:** Stores only non-sensitive academic data (Student ID, name, age, major) with no sensitive personal data collected[cite: 1].
4. **Modular and Reusable:** Built with decoupled classes and methods, making it easy to scale or adapt for other educational institutions[cite: 1].

## Example Usage & Output
When you run `assignment.py`, the terminal will display:
* System initialization info via the `@classmethod`.
* Success logs when student records are added into the dictionary structure.
* A formatted roster listing all enrolled students.
* Updates made to individual student majors via instance methods.
