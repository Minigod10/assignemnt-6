"""Write a Python function student_data () which will print the id of a student (student_id).
If the user passes an argument student_name or student_class the function will print the
student name and class."""
def student_data (student_name,student_class):
    print("student name: ",student_name,"\nstudent class: ",student_class)
student_data(input("Enter student name: "), input("Enter student class: "))