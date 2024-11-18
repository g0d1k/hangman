import tkinter as tk
import random

# Word list
word_list = [
    "Dog", "Cat", "Hat", "Sun", "Tree", "Car", "Fish", "Bird", "Moon", "Cup",
    "Apple", "Mop", "Star", "Bed", "Shoe", "Ball", "Fox", "Bush", "Frog", "Deer",
    "Rock", "Rain", "Cap", "Bed", "Fan", "Poo", "Bee", "Milk", "Start", "Cake",
    "Bus", "Pencil", "Spoon", "Van", "Pear", "Book", "Duck", "Egg", "Flag", "Ship",
    "Soap", "Lamp", "Bread", "Pot", "Rose", "Boot", "Mug", "Key", "Hand", "Nail",
    "Doll", "Bag", "Fig", "Hog", "Hat", "Net", "Nook", "Star", "Box", "Toad",
    "Boat", "Car", "Cup", "Pen", "Tree", "Boa", "Bat", "Fork", "Bell", "Sun",
    "Kite", "Drum", "Hen", "Ice", "Coat"
]

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("600x400")
        self.master.configure(bg="#f0f0f0")

        self.word = ""
        self.word_completion = ""
        self.guessed_letters = []
        self.tries = 8

        self.create_widgets()
        self.new_game()

    def create_widgets(self):
        # Word Display
        self.word_var = tk.StringVar()
        self.word_label = tk.Label(self.master, textvariable=self.word_var, font=("Arial", 24), bg="#f0f0f0")
        self.word_label.pack(pady=20)

        # Hangman Figure
        self.canvas = tk.Canvas(self.master, width=200, height=200, bg="#f0f0f0")
        self.canvas.pack(side=tk.LEFT, padx=20)

        # Guess Input
        self.guess_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.guess_frame.pack(pady=10)

        self.guess_entry = tk.Entry(self.guess_frame, font=("Arial", 14), width=5)
        self.guess_entry.grid(row=0, column=0, padx=5)
        self.guess_entry.bind("<Return>", self.submit_guess)

        self.guess_button = tk.Button(self.guess_frame, text="Guess", command=self.submit_guess)
        self.guess_button.grid(row=0, column=1, padx=5)

        # Guessed Letters Display
        self.guessed_var = tk.StringVar()
        self.guessed_label = tk.Label(self.master, textvariable=self.guessed_var, font=("Arial", 14), bg="#f0f0f0")
        self.guessed_label.pack(pady=10)

        # Tries Remaining
        self.tries_var = tk.StringVar()
        self.tries_label = tk.Label(self.master, textvariable=self.tries_var, font=("Arial", 14), bg="#f0f0f0")
        self.tries_label.pack()

        # Message Display
        self.message_var = tk.StringVar()
        self.message_label = tk.Label(self.master, textvariable=self.message_var, font=("Arial", 14), bg="#f0f0f0")
        self.message_label.pack(pady=10)

        # New Game and Quit Buttons
        self.button_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.button_frame.pack(side=tk.BOTTOM, pady=20)

        self.new_game_button = tk.Button(self.button_frame, text="New Game", command=self.new_game)
        self.new_game_button.grid(row=0, column=0, padx=10)

        self.quit_button = tk.Button(self.button_frame, text="Quit", command=self.master.quit)
        self.quit_button.grid(row=0, column=1, padx=10)

    def new_game(self):
        self.word = random.choice(word_list).lower()
        self.word_completion = "_" * len(self.word)
        self.guessed_letters = []
        self.tries = 8
        self.update_word_display()
        self.update_guessed_letters()
        self.update_tries_remaining()
        self.update_message("Good luck!")
        self.update_hangman_figure()
        self.guess_entry.delete(0, tk.END)
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_entry.focus()

    def submit_guess(self, event=None):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed_letters:
                self.update_message(f"You already guessed the letter {guess}")
            elif guess not in self.word:
                self.update_message(f"{guess} is not in the word.")
                self.tries -= 1
                self.guessed_letters.append(guess)
            else:
                self.update_message(f"Good job, {guess} is in the word!")
                self.guessed_letters.append(guess)
                word_as_list = list(self.word_completion)
                indices = [i for i, letter in enumerate(self.word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                self.word_completion = "".join(word_as_list)
        elif len(guess) == len(self.word) and guess.isalpha():
            if guess == self.word:
                self.word_completion = self.word
                self.update_message("Congratulations! You guessed the word!")
            else:
                self.update_message(f"{guess} is not the word.")
                self.tries -= 1
        else:
            self.update_message("Not a valid guess.")

        self.update_word_display()
        self.update_guessed_letters()
        self.update_tries_remaining()
        self.update_hangman_figure()

        if self.word_completion == self.word:
            self.update_message("Congratulations! You won!")
            self.guess_entry.config(state=tk.DISABLED)
        elif self.tries == 0:
            self.update_message(f"Sorry, you ran out of tries. The word was {self.word}.")
            self.guess_entry.config(state=tk.DISABLED)

    def update_word_display(self):
        self.word_var.set(" ".join(self.word_completion))

    def update_guessed_letters(self):
        self.guessed_var.set(f"Guessed letters: {', '.join(sorted(self.guessed_letters))}")

    def update_tries_remaining(self):
        self.tries_var.set(f"Tries remaining: {self.tries}")

    def update_message(self, message):
        self.message_var.set(message)

    def update_hangman_figure(self):
        self.canvas.delete("all")
        if self.tries < 8:
            self.canvas.create_line(20, 180, 180, 180)  # base
        if self.tries < 7:
            self.canvas.create_line(100, 180, 100, 20)  # pole
        if self.tries < 6:
            self.canvas.create_line(100, 20, 140, 20)   # top
        if self.tries < 5:
            self.canvas.create_line(140, 20, 140, 40)   # rope
        if self.tries < 4:
            self.canvas.create_oval(130, 40, 150, 60)   # head
        if self.tries < 3:
            self.canvas.create_line(140, 60, 140, 100)  # body
        if self.tries < 2:
            self.canvas.create_line(140, 80, 120, 70)   # left arm
            self.canvas.create_line(140, 80, 160, 70)   # right arm
        if self.tries < 1:
            self.canvas.create_line(140, 100, 120, 130) # left leg
            self.canvas.create_line(140, 100, 160, 130) # right leg

def main():
    root = tk.Tk()
    hangman_gui = HangmanGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
