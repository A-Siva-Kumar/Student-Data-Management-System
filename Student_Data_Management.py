# Student Data Management system::

''' FEATURES::
    Add Student details
        - student ID, Name, Age & Grade.
    view all the Students
    Search Students
    Update Students
    Delete Students
     '''


from numpy import delete


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

def search_detail(student,student_id):
    for stud in student:
        if stud.student_ID == student_id:
            print(stud)
    return " ID not found! "
    

# Update Student Details.

def update_detail(student, student_id, name = None, age = None, grade = None):
    for stud in student:
        if stud.student_ID == student_id:
            print("Before Updated: \n", stud)
            if name != None:
                stud.name = name
            if age != None:
                stud.age = age
            if grade != None:
                stud.grade = grade
            print(f" \nAfter Updated: \nStudent_ID: {student_id}, Name: {name}, Age: {age}, Grade: {grade} ")
    return " \nUpdated Successfully. "


# Delete Student.
        
def del_detail(student, student_id):
    for stud in student:
        if stud.student_ID == student_id:
            print(f'{stud} \n Deleted Successfully. ')
            return student.remove(stud)
        print (f" Student ID: {student_id} not found!")

# Main Body.
        
# creating list.

student_list= []

print("\n Welcome the SDM!🧐")

while True:
    # Choosing the Function...
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
        print(" Please enter the Details: ")
        student_id = int(input("ID : "))
        name = input("Name : ")
        age = int(input( "Age : "))
        grade = input( "Grade : " )
        add_details(student_list, student_id, name, age, grade)

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
        student_id = int(input("ID : "))
        name = input("Name : ")
        age = int(input( "Age : "))
        grade = input( "Grade : " )
        print(update_detail(student_list, student_id, name, age, grade))

    # Delete.
    elif function == 5:
            student_id = int(input("Student ID: "))
            print(del_detail(student_list,student_id))

    # Exit.
    else:
        print(" Exited Successfully. ")
        break

