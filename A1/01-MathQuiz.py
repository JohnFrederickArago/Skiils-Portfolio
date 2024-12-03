# Math Quiz
from tkinter import *
import random

# Create the main window
root = Tk()
root.title("Math Quiz") # Set the window title
root.geometry("500x500") # Set the window size
root.resizable(0, 0) # Disable window resizing
root.configure(bg="#493628") # Set the background color

# Global variables
difficulty = ''
score = 0
questions = 0
attempts = 0


# Reset the window
def reset_window():
    for widget in root.winfo_children(): # Destroy all widgets
        widget.destroy()


# Start the quiz
def start_quiz(level):
    # Reset global variables and display the first question
    global difficulty, score, questions, attempts
    difficulty = level
    score = 0
    questions = 0
    attempts = 0

    reset_window() # Clear the window
    display_problem() # Display the first question


# Random integer generator
def random_integer():
    # Return a random integer based on the difficulty
    min_val, max_val = {
        "Easy": (1, 9),
        "Moderate": (10, 99),
        "Hard": (100, 999)
    }[difficulty]
    return random.randint(min_val, max_val) # Return a random integer


# Random operation generator
def random_operation():
    return random.choice(['+', '-'])


# Displays the problem
def display_problem():
    global questions, score, attempts
    questions += 1
    attempts = 0

    # Check if the quiz should end after 10 questions
    if questions > 10:
        results(root)  
        return

    # Generate a random problem
    num1, num2 = random_integer(), random_integer()
    operation = random_operation()

    # Ensure no negative results
    if operation == '-':
        num1, num2 = sorted((num1, num2), reverse=True)

    # Calculate the correct answer
    correct_answer = eval(f"{num1} {operation} {num2}")
    question = f"{num1} {operation} {num2} = ?"

    reset_window() # Clear the window

    # Display the question
    question_label = Label(root, text=question, font=("Montserrat", 16), bg="#493628", fg="#E4E0E1")
    question_label.place(relx=0.5, rely=0.3, anchor=CENTER)
    # Display the answer entry
    answer_entry = Entry(root, width=10, font=("Montserrat", 14), bg="#D6C0B3", fg="#493628")
    answer_entry.place(relx=0.5, rely=0.4, anchor=CENTER)
    # Display the submit button
    submit_button = Button(root, text="Submit", font=("Montserrat", 14), bg="#E4E0E1", fg="#493628", width=10,
                           command=lambda: check_answer(answer_entry.get(), correct_answer, root))
    submit_button.place(relx=0.5, rely=0.5, anchor=CENTER)


# Checks the answer
def check_answer(selected, correct_answer, window):
    global score, attempts
    attempts += 1

    # Increase score if correct
    try:
        selected = int(selected)
        # 10 points for correct answer in one attempt, 5 points for correct answer in two attempts
        if selected == correct_answer:
            if attempts == 1:
                score += 10
            elif attempts == 2:
                score += 5
            result_text = "Correct!"
            result_color = "green"
            window.after(1500, lambda: display_problem()) # display next problem after 1.5 seconds
        else:
            # show two try again messages
            if attempts < 2:
                result_text = "Try Again!"
                result_color = "orange"
            else:
                result_text = "Incorrect!"
                result_color = "red"
                window.after(1500, lambda: display_problem())
    except ValueError:
        # show invalid message
        result_text = "Invalid!"
        result_color = "red"
        window.after(1500, lambda: display_problem())

    # Display the result
    result_label = Label(window, text=result_text, font=("Montserrat", 16), bg=result_color, fg="#E4E0E1")
    result_label.pack(pady=10)


# Displays the final results
def results(window):
    global score
    reset_window()

    # Display the final score
    final_score = Label(window, text=f"Final Score: {score}/100", font=("Montserrat", 16), bg="#493628", fg="#E4E0E1")
    final_score.place(relx=0.5, rely=0.3, anchor=CENTER)

    # Determine the rank
    if score >= 100:
        rank = "S"
    elif score >= 90:
        rank = "A+"
    elif score >= 80:
        rank = "A"
    elif score >= 70:
        rank = "B"
    elif score >= 60:
        rank = "C"
    else:
        rank = "D"
    
    # Display the rank
    rank_label = Label(window, text=f"Rank: {rank}", font=("Montserrat", 16), bg="#493628", fg="#E4E0E1")
    rank_label.place(relx=0.5, rely=0.4, anchor=CENTER)
    # Option to play again
    play_again_button = Button(window, text="Play Again", font=("Montserrat", 14), bg="#E4E0E1", fg="#493628", width=15, 
                               command=lambda: play_again(window))
    play_again_button.place(relx=0.5, rely=0.6, anchor=CENTER)
    # Option to leave
    close_button = Button(window, text="Leave", font=("Montserrat", 14), bg="#E4E0E1", fg="#493628", width=15, 
                          command=window.destroy)
    close_button.place(relx=0.5, rely=0.7, anchor=CENTER)

# Play again
def play_again(window):
    reset_window()
    setup_main_menu(window)


# Sets up the main menu
def setup_main_menu(window):
    # Set up the main menu
    label = Label(window, text="Math Quiz", font=("Montserrat", 30, "bold"), bg="#493628", fg="#E4E0E1")
    label.pack(pady=20)

    # Difficulty selection buttons
    button_style = {
        'font': ("Montserrat", 14),
        'bg': "#E4E0E1", 
        'fg': "#493628",
        'activebackground': "#82B3C9",  
        'activeforeground': "#1F4E79",
        'relief': "raised",
        'bd': 2,
        'width': 15,
        'highlightbackground': "#1F4E79"
    }
    button_easy = Button(window, text="Easy", command=lambda: start_quiz('Easy'), **button_style)
    button_easy.place(relx=0.5, rely=0.38, anchor=CENTER)
    button_moderate = Button(window, text="Moderate", command=lambda: start_quiz('Moderate'), **button_style)
    button_moderate.place(relx=0.5, rely=0.5, anchor=CENTER)
    button_hard = Button(window, text="Hard", command=lambda: start_quiz('Hard'), **button_style)
    button_hard.place(relx=0.5, rely=0.62, anchor=CENTER)


setup_main_menu(root) # Set up the main menu
root.mainloop() # Start the main loop