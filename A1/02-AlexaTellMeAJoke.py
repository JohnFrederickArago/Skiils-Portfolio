# Alexa Tell Me A Joke
import tkinter as tk
import random


# Joke and punchline dictionary
joke_punchline = {
    "Why did the chicken cross the road?": "To get to the other side.",
    "What happens if you boil a clown?": "You get a laughing stock.",
    "Why did the car get a flat tire?": "Because there was a fork in the road!",
    "How did the hipster burn his mouth?": "He ate his pizza before it was cool.",
    "What did the janitor say when he jumped out of the closet?": "SUPPLIES!!!!",
    "Have you heard about the band 1023MB?": "It's probably because they haven't got a gig yet…",
    "Why should you wear glasses to maths class?": "Because it helps with division.",
    "Why does it take pirates so long to learn the alphabet?": "Because they could spend years at C.",
    "Why did the woman go on the date with the mushroom?": "Because he was a fun-ghi.",
    "Why do bananas never get lonely?": "Because they hang out in bunches.",
    "What did the buffalo say when his kid went to college?": "Bison.",
    "Why shouldn't you tell secrets in a cornfield?": "Too many ears.",
    "What do you call someone who doesn't like carbs?": "Lack-Toast Intolerant.",
    "Why did the can crusher quit his job?": "Because it was soda pressing.",
    "Why did the birthday boy wrap himself in paper?": "He wanted to live in the present.",
    "What does a house wear?": "A dress.",
    "Why couldn't the toilet paper cross the road?": "Because it got stuck in a crack.",
    "Why didn't the bike want to go anywhere?": "Because it was two-tired!",
    "Want to hear a pizza joke?": "Nahhh, it's too cheesy!",  
    "Why are chemists great at solving problems?": "Because they have all of the solutions!",
    "Why is it impossible to starve in the desert?": "Because of all the sand which is there!",
    "What did the cheese say when it looked in the mirror?": "Halloumi!",
    "Why did the developer go broke?": "Because he used up all his cache.",
    "Did you know that ants are the only animals that don't get sick?": "It's true! It's because they have little antibodies.",
    "Why did the donut go to the dentist?": "To get a filling.",
    "What do you call a bear with no teeth?": "A gummy bear!",
    "What does a vegan zombie like to eat?": "Graaains.",
    "What do you call a dinosaur with only one eye?": "A Do-you-think-he-saw-us!",
    "Why should you never fall in love with a tennis player?": "Because to them... love means NOTHING!",
    "What did the full glass say to the empty glass?": "You look drunk.",
    "What's a potato's favorite form of transportation?": "The gravy train",
    "What did one ocean say to the other?": "Nothing, they just waved.",
    "What did the right eye say to the left eye?": "Honestly, between you and me something smells.",
    "What do you call a dog that's been run over by a steamroller?": "Spot!",
    "What's the difference between a hippo and a zippo?": "One's pretty heavy and the other's a little lighter",
    "Why don't scientists trust Atoms?": "They make up everything."}


# Function to display a random joke
def display_joke():
    global current_punchline # Keep track of the current punchline
    joke, current_punchline = random.choice(list(joke_punchline.items()))
    joke_result.config(text=joke + "\n") # Displays the joke
    punchline_button.config(state="normal") # Enables the punchline button
 

# Function to display the punchline to the joke
def display_punchline():
    joke_result.config(text=joke_result.cget("text") + current_punchline ) # Displays the punchline
    punchline_button.config(state="disabled") # Disables the punchline button


# Create the main window
root = tk.Tk()
root.title("Alexa Tell Me A Joke")
root.geometry("500x500")
root.resizable(0, 0)
root.configure(bg="#FFE6A9")


# Create the widgets
joke_result = tk.Label(root, text="", font=("Montserrat", 14), fg="#659287", bg="#FFE6A9", wraplength=420)
joke_result.place(relx=0.5, rely=0.3, anchor="center")

joke_button = tk.Button(root, text="Alexa Tell Me A Joke!", font=("Montserrat", 14), bg="#659287", fg="#FFE6A9", relief="raised", command=display_joke)
joke_button.place(relx=0.5, rely=0.6, anchor="center")

punchline_button = tk.Button(root, text="Show Punchline", font=("Montserrat", 14), bg="#659287", fg="#FFE6A9", relief="raised", command=display_punchline)
punchline_button.place(relx=0.5, rely=0.7, anchor="center")
punchline_button.config(state="disabled")


tk.mainloop() # Start the main loop