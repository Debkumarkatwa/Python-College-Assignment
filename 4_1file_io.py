# Open the file in write mode
with open('std_rec.txt', 'w') as file:
    print("Enter the student records. Enter '0' to stop.")

    # Write the header line
    file.write("stu_name,stu_roll,stu_marks\n")

    # Loop through each record
    while True:
        # Get the student details
        stu_name = input("Enter student name: ")
        if stu_name == '0':
            break
        stu_roll = input("Enter student roll number: ")
        stu_marks = input("Enter student marks: ")

        # Write the record to the file
        file.write(f"{stu_name},{stu_roll},{stu_marks}\n")

print("Student records have been written to 'std_rec.txt'.")