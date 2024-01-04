# Student Data Management system::

''' FEATURES::
    Add Student details
        - student ID, Name, Age & Grade.
    view all the Students
    Search Students
    Update Students
    Delete Students
     '''


class Student():
    def __init__(self, student_ID, name, age, grade):
        self.student_ID = student_ID
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
       return f"Student_ID: {self.student_ID}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


# Add Details.
def add_details(student_list, student_id, name, age, grade):
    add = Student(student_id, name, age, grade)
    student_list.append(add)
    print(f"\n Details:\n {add} \n Added Successfully.")


# Viewing all Students.
def view_details(student):
    if student == []:
        print(" No Data to Show... ")
    else:
        for i in student:
            print( i,"\n")
    return None


# Searching Student.
def search_detail(student_list,student_id):
    for stud in student_list:
        if stud.student_ID == student_id:
            print(stud)
            return " ID found."
    return " ID not found! "
    

# Update Student Details.
def update_detail(student_list, student_id, name = None, age = None, grade = None):
    for stud in student_list:
        if stud.student_ID == student_id:
            print("Before Updated: \n", stud)
            if name is not None:
                stud.name = name
            if age is not None:
                stud.age = age
            if grade is not None:
                stud.grade = grade
            return (f"\nAfter Updated: \nStudent_ID: {student_id}, Name: {name}, Age: {age}, Grade: {grade} ")
        return "\nUpdated Successfully. "
    return "\nID not found! "


# Delete Student.
def del_detail(student, student_id):
    for stud in student:
        if stud.student_ID == student_id:
            print(f'{stud} \nDeleted Successfully. ')
            return student.remove(stud)
        print (f" Student ID: {student_id} not found!")

        
# Validating Age...
def valid_input(message):
    while True:
        try:
            Input = int(input(message))
            if Input > 0:
                return Input
        except ValueError:
            print("Invalid input. Please enter Correct Age 🗓️ ")
    
# Taking Inputs..
def take_input():
    student_id = valid_input("Enter ID: ")
    name = input("Name : ")
    age = valid_input("Enter Age: ")
    grade = input( "Grade : " )
    return student_id, name, age, grade

# creating list.
student_list= []
print("\n Welcome the SDM!🧐")


# Choosing the Function...
while True:
    
    print("\n Choose the Option: ")
    print(''' 
        1. Add Student.
        2. View all Student.
        3. Search Student.
        4. Update Student.
        5. Delete Student.
        6. Exit
        ''')

    # Taking Option Input.
    function = int(input(" Enter Option: "))

    # Performing the functions.

    # Add.
    if function == 1: 
        print("Please enter the Details: ")
        student_id, name, age, grade = take_input()
        add_details(student_list, student_id, name , age, grade)

    # View.
    elif function == 2:
        print(" \n Details of all Students: \n ")
        view_details(student_list)

    # Search.
    elif function == 3:
        student_id = int(input("Student ID: "))
        search_detail(student_list, student_id)

    # Update.
    elif function == 4:
        student_id, name, age, grade = take_input()
        print(update_detail(student_list, student_id, name, age, grade))

    # Delete.
    elif function == 5:
            student_id = int(input("Student ID: "))
            print(del_detail(student_list,student_id))

    # Exit.
    else:
        print(" Exited Successfully. ")
        break

