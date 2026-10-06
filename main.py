class Student:
    """
    Task 1: Represents an individual student in the Education domain.
    """
    def __init__(self, student_id, name, age, major):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    # Task 3: Instance Method (operates on an individual student instance)
    def display_info(self):
        print(f"ID: {self.student_id} | Name: {self.name} | Age: {self.age} | Major: {self.major}")

    # Additional Instance Method to update student records securely (DPG privacy principle)
    def update_major(self, new_major):
        self.major = new_major
        print(f"Record updated: {self.name}'s major is now {self.major}.")


class StudentPortal:
    """
    Task 2: Uses a Dictionary data structure to store multiple Student objects.
    Task 3: Implements a @classmethod to handle system-level metadata.
    """
    system_name = "Digital Public Goods Student Portal"

    def __init__(self):
        # Dictionary data structure using unique student IDs as keys
        self.records = {}

    def add_record(self, student_id, name, age, major):
        """Function to add a student record to the dictionary structure."""
        if student_id in self.records:
            print(f"Error: Student with ID {student_id} already exists.")
        else:
            new_student = Student(student_id, name, age, major)
            self.records[student_id] = new_student
            print(f"Success: Added {name} to system records.")

    def display_records(self):
        """Function to display all records stored in the dictionary."""
        if not self.records:
            print("No student records found.")
        else:
            print("\n--- All Student Records ---")
            for student_id, student_obj in self.records.items():
                student_obj.display_info()

    # Task 3: Class Method (@classmethod) - interacts with the class scope (cls)
    @classmethod
    def get_system_info(cls):
        print(f"\n[System Info] Running: {cls.system_name} (Aligned with DPG Standards)")


# --- Program Execution ---
if __name__ == "__main__":
    # Call the Class Method
    StudentPortal.get_system_info()

    # Initialize portal
    portal = StudentPortal()

    # Add records using Task 2 dictionary structure
    portal.add_record("ED101", "Fatmata Jalloh", 19, "Computer Science")
    portal.add_record("ED102", "Ibrahim Sesay", 21, "Information Technology")

    # Display records
    portal.display_records()

    # Demonstrate Instance Method update (Task 3)
    print("\n--- Executing Instance Method Update ---")
    student_to_update = portal.records.get("ED101")
    if student_to_update:
        student_to_update.update_major("Software Engineering")
        student_to_update.display_info()
