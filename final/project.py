import json
import tkinter as tk
from tkinter import simpledialog, messagebox
import random
import os
from PIL import Image, ImageTk


# function getting the questions for the json file
def load_questions(file):
    try:
        with open(file, "r") as file:
            data = json.load(file)
        return data["quiz"]
    except (FileNotFoundError, json.JSONDecodeError) as error:
        messagebox.showerror("Error", f"failed to load questions {error}")

# function to filter the questions depending on the difficulty
def questions_by_difficulty(questions, difficulty):
    filtered_questions = []
    for question in questions:
        if question["level"] == difficulty:
            filtered_questions.append(question)
    return filtered_questions

# function for cheeking the answer
def check_answer(question, answer):
    return answer == question["answer"]

# function to get a message depending on the score
def message(score, total, difficulty):
    percent = (score / total) * 100

    if difficulty == "easy":
        if percent == 100:
            return "Perfect! Are you a wizard or something? 🧙‍♂️✨"
        elif percent >= 80:
            return "Amazing! You're ready for your first year at Hogwarts! 🦉📚"
        elif percent >= 60:
            return "Nice work! You’d totally pass your first Charms class! ✨📖"
        elif percent >= 40:
            return "Not bad! You're getting the hang of it! ✨🔮"
        else:
            return "Hmm... Time to reread the books again! 📚🔍"

    elif difficulty == "medium":
        if percent == 100:
            return "Perfect! You're a true Hogwarts professor! 🎓🧙‍♂️"
        elif percent >= 80:
            return "Amazing! You're ready for your O.W.L.s! 🦉📜"
        elif percent >= 60:
            return "Nice work! You could totally survive the Triwizard Tournament (hopefully). 🏆🔥"
        elif percent >= 40:
            return "Not bad! Keep studying those potions—Snape is watching! 🧪👀"
        else:
            return "Oh dear… even Gilderoy Lockhart might have scored higher! 😬📖"

    elif difficulty == "hard":
        if percent == 100:
            return "Outstanding! You could give Dumbledore a run for his Galleons! 🧙‍♂️💰"
        elif percent >= 80:
            return "Amazing! You're ready to take on Voldemort! 🐍⚡"
        elif percent >= 60:
            return "Great job! You’re mastering advanced spells!🔥📜"
        elif percent >= 40:
            return "Not bad! But maybe avoid challenging Hermione to a duel😅"
        else:
            return "Yikes… did someone hex you? Better get to Madam Pomfrey! 🏥🌀"

    else:
        return "Oops! Looks like you tried casting 'Expecto Difficultum'—but it backfired! 💥🔮"

    
# function for the next and next and next and...(you got the idea) question
def next_question():
    global current_question, score
    if current_question < len(questions):
        question_number_label.config(
            text=f"Question {current_question + 1} of {len(questions)}")

        question = questions[current_question]
        question_label.config(text=question["question"])
        for i, option in enumerate(question["options"]):
            option_buttons[i].config(
                text=option, state=tk.NORMAL, bg="SystemButtonFace", fg="black")
            option_buttons[i].config(command=lambda i=i: select_answer(i))
        current_question += 1
    else:
        question_number_label.pack_forget()
        question_label.pack_forget()
        for button in option_buttons:
            button.pack_forget()

        meme_image = meme()
        if meme_image:
            meme_label.config(image=meme_image)
            meme_label.image = meme_image
            meme_label.pack(pady=10)

        quirky_message = message(score, len(questions), difficulty)
        score_label.config(text=f"Final Score: {score}/{len(questions)}")
        message_label.config(text=quirky_message)
        restart_button.pack(pady=10)

# handling answers
def select_answer(selected_option):
    global score
    question = questions[current_question - 1]
    user_answer = question["options"][selected_option]
    if check_answer(question, user_answer):
        score += 1
        option_buttons[selected_option].config(bg="#006400", fg="white")
    else:
        option_buttons[selected_option].config(bg="#8B0000", fg="white")
        correct_index = question["options"].index(question["answer"])
        option_buttons[correct_index].config(bg="#006400", fg="white")
    score_label.config(text=f"Score: {score}/{len(questions)}")
    for button in option_buttons:
        button.config(state=tk.DISABLED)
    root.after(1000, next_question)

# function to retsrt the quiz
def restart():
    global current_question, score, questions, difficulty

    # reseting the variables
    current_question = 0
    score = 0

    # cleaning the visiual elements
    meme_label.pack_forget()
    restart_button.pack_forget()
    message_label.config(text="")

    # asking for difficulty again
    difficulty = simpledialog.askstring("Difficulty", "Choose difficulty (easy, medium, hard):")
    if difficulty not in ["easy", "medium", "hard"]:
        messagebox.showerror("Error", "Please enter a valid difficulty.")
        root.quit()
        return

    # loading questions by choosen difficulty
    questions = questions_by_difficulty(load_questions("quiz.json"), difficulty)
    if not questions:
        messagebox.showerror("Error", "No questions at this difficulty.")
        root.quit()
        return

    random.shuffle(questions)

    # re-show the visible elments
    question_number_label.pack(pady=10)
    question_label.pack(pady=10)
    score_label.pack(pady=10)
    message_label.pack(pady=10)
    for button in option_buttons:
        button.pack(pady=5)

    # displaying  the first question
    next_question()


# get memed hehe 😂
def meme():
    meme_folder = "memes"
    if os.path.exists(meme_folder) and os.path.isdir(meme_folder):
        meme_files = [file for file in os.listdir(meme_folder) if file.lower(
        ).endswith((".png", ".jpg", ".jpeg", ".webp", ".gif"))]
        if meme_files:
            meme_file = random.choice(meme_files)
            meme_path = os.path.join(meme_folder, meme_file)
            try:
                meme_image = Image.open(meme_path)
                meme_image = meme_image.resize(
                    (300, 300), Image.Resampling.LANCZOS)
                return ImageTk.PhotoImage(meme_image)
            except Exception as error:
                print(f"Failed to get memed: {error}")
    return None


# the main function
def main():
    global root, question_label, option_buttons, score_label,  message_label, score, questions
    global current_question, difficulty, question_number_label, meme_label, restart_button

    root = tk.Tk()
    root.title("Harry Potter Quiz")
    root.geometry("500x650")

   # setting up the iconic snitch
    try:
        icon = Image.open("golden_snitch.webp")
        icon = ImageTk.PhotoImage(icon)
        root.iconphoto(True, icon)
    except FileNotFoundError:
        messagebox.showerror("Error", "Golden Snich hasn't been caught.")
        root.quit()
        return

    # asking for difficulty
    difficulty = simpledialog.askstring(
        "Difficulty", "Choose difficulty (easy, medium, hard):")
    if difficulty not in ["easy", "medium", "hard"]:
        messagebox.showerror("Error", "Please enter a valid difficulty.")
        root.quit()
        return

    # loading questions by choosen difficulty
    questions = questions_by_difficulty(
        load_questions("quiz.json"), difficulty)
    if not questions:
        messagebox.showerror("Error", "No questions at this difficulty.")
        root.quit()
        return

    random.shuffle(questions)

    # inisialising veriables
    current_question = 0
    score = 0

    # elements
    question_number_label = tk.Label(root, text="", font=("Arial", 12))
    question_number_label.pack(pady=10)

    question_label = tk.Label(
        root, text="", wraplength=450, font=("Arial", 12))
    question_label.pack(pady=10)

    score_label = tk.Label(
        root, text=f"Score: {score}/{len(questions)}", font=("Arial", 12))
    score_label.pack(pady=10)

    # for windows not sure if it works for other operating systems
    message_label = tk.Label(root, text="", wraplength=450, font=(
        "Segoe UI Emoji", 12), fg="#301934")
    message_label.pack(pady=10)

    option_buttons = []
    for _ in range(4):
        button = tk.Button(root, text="", width=30, font=("Arial", 10))
        button.pack(pady=5)
        option_buttons.append(button)

    meme_label = tk.Label(root)

    restart_button = tk.Button(
        root, text="Restart Quiz", command=restart, font=("Arial", 12))

    next_question()
    root.mainloop()


if __name__ == "__main__":
    main()
