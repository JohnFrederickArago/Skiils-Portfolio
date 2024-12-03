# Student Record's Manager
import tkinter as tk
from tkinter import ttk 
from tkinter import *
import os # Import the os module
    

# Load student records from the txt file
def load_file(file_path):
    if not os.path.isfile(file_path): # Check if file exists
        return []
        
    with open(file_path, 'r') as file: # Open the file
        lines = file.readlines()
        
    students = [] # Create a list to store the student records
    for line in lines[1:]:  # Skip header
        values = line.strip().split(',') # Split each line
        if len(values) < 3: # Check if there are enough values
            print(f"Skipping invalid line: {line}")
            continue
        student_id, name, *coursework, exam = values # Unpack values
        coursework = list(map(int, coursework)) # Convert coursework marks to floating-point numbers
        exam = float(exam) # Convert exam mark to floating-point number
        coursework_total = sum(coursework)
        overall_total = coursework_total + exam 
        percentage = round((overall_total / 160) * 100, 2)
        final_grade = calculate_grade(percentage)
        student_record = (student_id, name, coursework_total, exam, percentage, final_grade) # Create student record
        students.append(student_record) # Add student record to the list
    return students # Return the list of student records


# Clear the text display
def clear_display():
    text_display.delete(1.0, tk.END)


# Calculate grade
def calculate_grade(percentage):
    if percentage >= 70:
        return 'A'
    elif percentage >= 60:
        return 'B'
    elif percentage >= 50:
        return 'C'
    elif percentage >= 40:
        return 'D'
    else:
        return 'F'


# Display all records
def display_all_records():
    clear_display()
    text = ""
    for student in students: # Loop through the list of student records
        student_name = student[1]
        student_number = student[0]
        coursework_total = student[2]
        exam_mark = student[3]
        overall_percentage = student[4]
        grade = student[5]
        # Add student record to the text
        text += ( 
            f"Name: {student_name}\nStudent Number: {student_number}\n"
            f"Total Coursework Mark: {coursework_total}\nExam Mark: {exam_mark}\n"
            f"Overall Percentage: {overall_percentage:.2f}%\nGrade: {grade}\n\n"
        )
    # Add total number of students and average percentage
    if students:
        total_percentage = sum(student[4] for student in students)
        num_students = len(students)
        avg_percentage = total_percentage / num_students
        text += (
            f"\n\nNumber of Students: {num_students}"
            f"\nAverage Percentage: {avg_percentage:.2f}%\n"
        )
    text_display.insert(tk.END, text + " ") # Insert the text into the text display


# Displays highest score
def display_highest_score():
    highest_score = max(students, key=lambda student: student[4])
    display_one_student(highest_score)


# Displays lowest score
def display_lowest_score():
    lowest_score = min(students, key=lambda student: student[4])
    display_one_student(lowest_score)


# Displays one student
def display_one_student(student):
    clear_display()
    # Extract the student's information
    student_name = student[1]
    student_number = student[0]
    coursework_total = student[2]
    exam_mark = student[3]
    overall_percentage = student[4]
    grade = student[5]
    # Create the text to display
    student_info = (
        f"Name: {student_name}\n"
        f"Student Number: {student_number}\n"
        f"Total Coursework Mark: {coursework_total}\n"
        f"Exam Mark: {exam_mark}\n"
        f"Overall Percentage: {overall_percentage:.2f}%\n"
        f"Grade: {grade}\n"
    )
    text_display.insert(tk.END, student_info) # Insert the text into the text display


# Displays dropdown
def view_dropdown():
    selected_index = student_dropdown.current() # Get the index of the selected student
    # If a student is selected
    if selected_index != -1:
        selected_student = students[selected_index] # Get the selected student
        display_one_student(selected_student) # Display the selected student


# Ascending sort
def sort_records_ascending():
    global students
    students.sort(key=lambda student: student[4], reverse=True) # Sort the list of student records by overall percentage
    display_all_records()
    return students


# Descending sort
def sort_records_descending():
    global students
    students.sort(key=lambda student: student[4], reverse=False) # Sort the list of student records by overall percentage
    display_all_records()
    return students # Return the list of student records


# Add student
def add_student():
    open_new_window()


def delete_student():
    global students
    selected_index = student_dropdown.current() # Get the index of the selected student
    if 0 <= selected_index < len(students):
        student_id = students[selected_index][0]
        del students[selected_index]
        student_dropdown['values'] = [student[1] for student in students]
        student_dropdown.current(len(students)-1)

        # Delete the selected student from the file
        with open("A1/Data/studentMarks.txt", "r+") as f:
            lines = f.readlines() # Read the file
            f.seek(0) # Set the file pointer to the beginning
            # Write all lines except the selected student
            for line in lines:
                if not line.startswith(str(student_id) + ','):
                    f.write(line)
            f.truncate() # Truncate the file

        students = load_file("A1/Data/studentMarks.txt") # Reload the student records
        display_all_records() # Display updated records
        

def update_student():
    selected_index = student_dropdown.current() # Get the index of the selected student
    # If a student is selected
    if 0 <= selected_index < len(students):
        student_id = students[selected_index][0]
        student_name = students[selected_index][1]
        coursework_total = students[selected_index][2]
        exam_mark = students[selected_index][3]
        
        win = Tk()
        win.geometry("450x500")
        win.title("Update Student")
        win.resizable(0,0)
        win.configure(bg="#F1F0E8")

        # Create labels and entry fields
        id_label = Label(win, text="Enter ID", width=20, font=("montesserat",12), anchor="w", bg="#F1F0E8")
        id_label.place(x=20, y=120)
        en1 = Entry(win, width=25, font=("montesserat",12), bg="#525B44", fg="white")
        en1.insert(0, str(student_id))
        en1.place(x=200, y=120)

        name_label = Label(win, text="Enter Name", width=20, font=("montesserat",12), anchor="w", bg="#F1F0E8")
        name_label.place(x=20, y=150)
        en3 = Entry(win, width=25, font=("montesserat",12), bg="#525B44", fg="white")
        en3.insert(0, student_name)
        en3.place(x=200, y=150)

        coursework_label = Label(win, text="Enter Coursework Total", width=20, font=("montesserat",12), anchor="w", bg="#F1F0E8")
        coursework_label.place(x=20, y=180)
        en4 = Entry(win, width=25, font=("montesserat",12), bg="#525B44", fg="white")
        en4.insert(0, str(coursework_total))
        en4.place(x=200, y=180)

        exam_label = Label(win, text="Enter Exam Mark", width=20, font=("montesserat",12), anchor="w", bg="#F1F0E8")
        exam_label.place(x=20, y=210)
        en5 = Entry(win, width=25, font=("montesserat",12), bg="#525B44", fg="white")
        en5.insert(0, str(exam_mark))
        en5.place(x=200, y=210)

        # Save details button
        def save_details():
            global students # Access the global variable

            # Get the new values from the entry fields
            new_id = int(en1.get())
            new_name = en3.get()
            new_coursework_total = int(en4.get())
            new_exam_mark = float(en5.get())
            # Calculate the new overall percentage
            new_overall_percentage = round((new_coursework_total + new_exam_mark) / 160 * 100, 2)
            # Calculate the new grade
            new_grade = calculate_grade(new_overall_percentage)

            # Update the student record
            students[selected_index] = [
                new_id,
                new_name,
                new_coursework_total,
                new_exam_mark,
                new_overall_percentage,
                new_grade
            ]

            # Update the student dropdown
            with open("A1/Data/studentMarks.txt", "r+") as f:
                lines = f.readlines() # Read the file
                f.seek(0) # Set the file pointer to the beginning
                # Write all lines except the selected student
                for line in lines:
                    if line.startswith(str(student_id) + ','):
                        f.write(f"{en1.get()},{en3.get()},{new_coursework_total//3},{new_coursework_total//3},{new_coursework_total//3},{en5.get()}\n")
                    else:
                        f.write(line)
                f.truncate() # Truncate the file
            students = load_file("A1/Data/studentMarks.txt") # Reload the student records
            display_all_records()
            win.destroy() # Close the window
            
        # Save button
        save_button = Button(win, text="Save", bg="#525B44", fg="white", width=10, command=save_details, font=("montesserat",12))
        save_button.place(relx=0.5, rely=0.6, anchor=CENTER)


# Open new window
def open_new_window():
    # Create a new window
    win = Tk()  
    win.geometry("450x500")  
    win.title("Add Student")
    win.resizable(0,0)
    win.configure(bg="#F1F0E8")  

    # Create labels and entry fields
    id= Label(win, text="Enter ID", width=20, font=("montesserat",12), anchor="w", bg="#F1F0E8")  
    id.place(x=19, y=60)  
    en1= Entry(win, width=25, bg="#525B44", fg="white", font=("montesserat",12))  
    en1.place(x=200, y=60)  

    name= Label(win, text="Enter Name", width=20, font=("montesserat",12), anchor="w", bg="#F1F0E8") 
    name.place(x=19, y=100)  
    en3= Entry(win, width=25, bg="#525B44", fg="white", font=("montesserat",12))  
    en3.place(x=200, y=100)  

    coursework1= Label(win, text="Coursework 1", width=20,font=("montesserat",12), anchor="w", bg="#F1F0E8") 
    coursework1.place(x=19, y=140)  
    en4= Entry(win, width=25, bg="#525B44", fg="white", font=("montesserat",12))  
    en4.place(x=200, y=140)  

    coursework2= Label(win, text="Coursework 2", width=20,font=("montesserat",12), anchor="w", bg="#F1F0E8")
    coursework2.place(x=19, y=180)  
    en5= Entry(win, width=25, bg="#525B44", fg="white", font=("montesserat",12))  
    en5.place(x=200, y=180) 

    coursework3= Label(win, text="Coursework 3", width=20,font=("montesserat",12), anchor="w", bg="#F1F0E8")  
    coursework3.place(x=19, y=220)  
    en6= Entry(win, width=25, bg="#525B44", fg="white", font=("montesserat",12))  
    en6.place(x=200, y=220)

    exam = Label(win, text="Exam", width=20,font=("montesserat",12), anchor="w", bg="#F1F0E8")
    exam.place(x=19, y=260)  
    en7= Entry(win, width=25, bg="#525B44", fg="white", font=("montesserat",12))  
    en7.place(x=200, y=260)
    
    # Adds to the file
    def add_to_file():
        with open("A1/Data/studentMarks.txt", "a") as f:
            f.write(f"\r{en1.get()},{en3.get()},{en4.get()},{en5.get()},{en6.get()},{en7.get()}")
        global students
        students = load_file("A1/Data/studentMarks.txt") # Reload the student records
        display_all_records() # Display updated records
        student_dropdown['values'] = [student[1] for student in students] # Update the student dropdown
        win.destroy()

    # Add button
    Button(win, text="Add", bg="#525B44", fg="white", width=10, command=add_to_file, font=("montesserat",12)).place(relx=0.5, rely=0.7, anchor=CENTER)
    win.mainloop()



students = load_file('A1/Data/studentMarks.txt') # Load student records 


# Create the main window
root = tk.Tk()
root.title("Student Record's Manager")
root.geometry("1000x700")
root.configure(bg="#F1F0E8")
root.resizable(0, 0)


# Heading
title_label = tk.Label(root, text="Student Record's Manager", font=("Montserrat", 18, "bold"), bg="#525B44", fg="white", padx=15, pady=15)
title_label.pack(side="top", fill="x")

# Button Frames
buttons = tk.Frame(root, padx=20, pady=20)
buttons.pack(side="left", fill="y")

# Three buttons
tk.Frame(buttons, height=40).pack()
tk.Button(buttons, text="View All Records", command=display_all_records, anchor="center", bg="#525B44", fg="white", padx=5, pady=5, font=("Montserrat", 10)).pack(pady=10, fill="x")
tk.Button(buttons, text="Highest Score", command=display_highest_score, anchor="center", bg="#525B44", fg="white", padx=5, pady=5, font=("Montserrat", 10)).pack(pady=10, fill="x")
tk.Button(buttons, text="Lowest Score", command=display_lowest_score, anchor="center", bg="#525B44", fg="white", padx=5, pady=5, font=("Montserrat", 10)).pack(pady=10, fill="x")
tk.Button(buttons, text="Ascending", command=sort_records_ascending, anchor="center", bg="#525B44", fg="white", padx=5, pady=5, font=("Montserrat", 10)).pack(pady=10, fill="x")
tk.Button(buttons, text="Descending", command=sort_records_descending, anchor="center", bg="#525B44", fg="white", padx=5, pady=5, font=("Montserrat", 10)).pack(pady=10, fill="x")
tk.Button(buttons, text="Add Student", command=add_student, anchor="center", bg="#525B44", fg="white", padx=5, pady=5, font=("Montserrat", 10)).pack(pady=10, fill="x")
tk.Button(buttons, text="Exit", command=root.quit, anchor="center", bg="#525B44", fg="white", padx=5, pady=5, font=("Montserrat", 10)).pack(pady=10, fill="x")

# Student Frame
student_frame = tk.Frame(root)
student_frame.pack(side="top", fill="x")

student_label = tk.Label(student_frame, text="View individual student record", font=("Montserrat", 10), anchor="w")
student_label.pack(side="left", padx=5, pady=5)

# Dropdown
student_dropdown = ttk.Combobox(student_frame, values=[student[1] for student in students], state="readonly")
student_dropdown.set("Select a student")
student_dropdown.configure(font=("Montserrat", 10), justify="center")
student_dropdown.pack(side="left", pady=10)

tk.Frame(student_frame, width=15).pack(side="left", fill="y")

# View button
tk.Button(student_frame, text="View", command=view_dropdown, anchor="center", bg="#525B44", fg="white", padx=15, pady=5, font=("Montserrat", 10)).pack(side="left", pady=5)
tk.Button(student_frame, text="Delete", command=delete_student, anchor="center", bg="#525B44", fg="white", padx=10, pady=5, font=("Montserrat", 10)).pack(side="left", pady=5, padx=10)
tk.Button(student_frame, text="Update", command=update_student, anchor="center", bg="#525B44", fg="white", padx=10, pady=5, font=("Montserrat", 10)).pack(side="left", pady=5)

# Text display
text_display = tk.Text(root, height=20, width=80, bg="#525B44", fg="white", font=("Montserrat", 10), padx=10, pady=10)
text_display.pack(side="right", fill="both", expand=True, padx=20, pady=20)


root.mainloop() # Start the main loop