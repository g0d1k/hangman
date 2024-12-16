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
    "Kite", "Drum", "Hen", "Ice", "Coat", "Basket", "Rocket", "Jungle", "Quilt", "Market", "Forest", "Spirit", "Wonder", 
    "Guitar", "Orange", "Secret", "Dragon", "Castle", "Bridge", "Garden", "Pirate", 
    "Animal", "Candle", "Elephant", "Subway", "Ocean", "Friend", "Spring", "Bottle", 
    "Copper", "Giraffe", "Summer", "Pocket", "Jacket", "Fancy", "Monster", "Falcon", 
    "Planet", "Ticket", "Robot", "Banana", "Soccer", "Bishop", "Camera", "Double", "Garlic", "abruptly",
    "able", "about", "account", "acid", "across", "act", "addition", "adjustment", "advertisement", "after", "again", 
    "against", "agreement", "air", "all", "almost", "among", "amount", "amusement", "and", "angle", "angry", "animal", 
    "answer", "ant", "any", "apparatus", "apple", "approval", "arch", "argument", "arm", "army", "art", "as", "at", 
    "attack", "attempt", "attention", "attraction", "authority", "automatic", "awake", "baby", "back", "bad", "bag", "balance", 
    "ball", "band", "base", "basin", "basket", "bath", "be", "beautiful", "because", "bed", "bee", "before", "behaviour", "belief", 
    "bell", "bent", "berry", "between", "bird", "birth", "bit", "bite", "bitter", "black", "blade", "blood", "blow", "blue", "board", "boat", 
    "body", "boiling", "bone", "book", "boot", "bottle", "box", "boy", "brain", "brake", "branch", "brass", "bread", "breath", 
    "brick", "bridge", "bright", "broken", "brother", "brown", "brush", "bucket", "building", "bulb", "burn", "burst", "business", "but", 
    "butter", "button", "by", "cake", "camera", "canvas", "card", "care", "carriage", "cart", "cat", "cause", "certain", "chain", "chalk", 
    "chance", "change", "cheap", "cheese", "chemical", "chest", "chief", "chin", "church", "circle", "clean", "clear", "clock", "cloth", "cloud", 
    "coal", "coat", "cold", "collar", "colour", "comb", "come", "comfort", "committee", "common", "company", "comparison", "competition", 
    "complete", "complex", "condition", "connection", "conscious", "control", "cook", "copper", "copy", "cord", "cork", "cotton", "cough", "country", 
    "cover", "cow", "crack", "credit", "crime", "cruel", "crush", "cry", "cup", "cup", "current", "curtain", "curve", "cushion", "damage", "danger", 
    "dark", "daughter", "day", "dead", "dear", "death", "debt", "decision", "deep", "degree", "delicate", "dependent", "design", "desire", "destruction", 
    "detail", "development", "different", "digestion", "direction", "dirty", "discovery", "discussion", "disease", "disgust", "distance", "distribution", 
    "division", "do", "dog", "door", "doubt", "down", "drain", "drawer", "dress", "drink", "driving", "drop", "dry", "dust", "ear", "early", "earth", 
    "east", "edge", "education", "effect", "egg", "elastic", "electric", "end", "engine", "enough", "equal", "error", "even", "event", "ever", "every", 
    "example", "exchange", "existence", "expansion", "experience", "expert", "eye", "face", "fact", "fall", "false", "family", "far", "farm", "fat", "father", 
    "fear", "feather", "feeble", "feeling", "female", "fertile", "fiction", "field", "fight", "finger", "fire", "first", "fish", "fixed", "flag", "flame", "flat", 
    "flight", "floor", "flower", "fly", "fold", "food", "foolish", "foot", "for", "force", "fork", "form", "forward", "fowl", "frame", "free", "frequent", 
    "friend", "from", "front", "fruit", "full", "future", "garden", "general", "get", "girl", "give", "glass", "glove", "go", "goat", "gold", "good", 
    "government", "grain", "grass", "great", "green", "grey", "grip", "group", "growth", "guide", "gun", "hair", "hammer", "hand", "hanging", "happy", 
    "harbour", "hard", "harmony", "hat", "hate", "have", "he", "head", "healthy", "hear", "hearing", "heart", "heat", "help", "high", "history", "hole", 
    "hollow", "hook", "hope", "horn", "horse", "hospital", "hour", "house", "how", "humour", "I", "ice", "idea", "if", "ill", "important", "impulse", "in", 
    "increase", "industry", "ink", "insect", "instrument", "insurance", "interest", "invention", "iron", "island", "jelly", "jewel", "join", "journey", 
    "judge", "jump", "keep", "kettle", "key", "kick", "kind", "kiss", "knee", "knife", "knot", "knowledge", "land", "language", "last", "late", "laugh", 
    "law", "lead", "leaf", "learning", "leather", "left", "leg", "let", "letter", "level", "library", "lift", "light", "like", "limit", "line", "linen", 
    "lip", "liquid", "list", "little", "living", "lock", "long", "look", "loose", "loss", "loud", "love", "low", "machine", "make", "male", "man", "manager", 
    "map", "mark", "market", "married", "mass", "match", "material", "may", "meal", "measure", "meat", "medical", "meeting", "memory", "metal", "middle", 
    "military", "milk", "mind", "mine", "minute", "mist", "mixed", "money", "monkey", "month", "moon", "morning", "mother", "motion", "mountain", "mouth", 
    "move", "much", "muscle", "music", "nail", "name", "narrow", "nation", "natural", "near", "necessary", "neck", "need", "needle", "nerve", "net", "new", 
    "news", "night", "no", "noise", "normal", "north", "nose", "not", "note", "now", "number", "nut", "observation", "of", "off", "offer", "office", "oil", 
    "old", "on", "only", "open", "operation", "opinion", "opposite", "or", "orange", "order", "organization", "ornament", "other", "out", "oven", "over", 
    "owner", "page", "pain", "paint", "paper", "parallel", "parcel", "part", "past", "paste", "payment", "peace", "pen", "pencil", "person", "physical", 
    "picture", "pig", "pin", "pipe", "place", "plane", "plant", "plate", "play", "please", "pleasure", "plough", "pocket", "point", "poison", "polish", 
    "political", "poor", "porter", "position", "possible", "pot", "potato", "powder", "power", "present", "price", "print", "prison", "private", "probable", 
    "process", "produce", "profit", "property", "prose", "protest", "public", "pull", "pump", "punishment", "purpose", "push", "put", "quality", "question", 
    "quick", "quiet", "quite", "rail", "rain", "range", "rat", "rate", "ray", "reaction", "reading", "ready", "reason", "receipt", "record", "red", "regret", 
    "regular", "relation", "religion", "representative", "request", "respect", "responsible", "rest", "reward", "rhythm", "rice", "right", "ring", "river", 
    "road", "rod", "roll", "roof", "room", "root", "rough", "round", "rub", "rule", "run", "sad", "safe", "sail", "salt", "same", "sand", "say", "scale", 
    "school", "science", "scissors", "screw", "sea", "seat", "second", "secret", "secretary", "see", "seed", "seem", "selection", "self", "send", "sense", 
    "separate", "serious", "servant", "sex", "shade", "shake", "shame", "sharp", "sheep", "shelf", "ship", "shirt", "shock", "shoe", "short", "shut", "side", 
    "sign", "silk", "silver", "simple", "sister", "size", "skin", "skirt", "sky", "sleep", "slip", "slope", "slow", "small", "smash", "smell", "smile", "smoke", 
    "smooth", "snake", "sneeze", "snow", "so", "soap", "society", "sock", "soft", "solid", "some", "son", "song", "sort", "sound", "soup", "south", "space", 
    "spade", "special", "sponge", "spoon", "spring", "square", "stage", "stamp", "star", "start", "statement", "station", "steam", "steel", "stem", "step", 
    "stick", "sticky", "stiff", "still", "stitch", "stocking", "stomach", "stone", "stop", "store", "story", "straight", "strange", "street", "stretch", 
    "strong", "structure", "substance", "such", "sudden", "sugar", "suggestion", "summer", "sun", "support", "surprise", "sweet", "swim", "system", "table", 
    "tail", "take", "talk", "tall", "taste", "tax", "teaching", "tendency", "test", "than", "that", "the", "then", "theory", "there", "thick", "thin", "thing", 
    "this", "thought", "thread", "throat", "through", "through", "thumb", "thunder", "ticket", "tight", "till", "time", "tin", "tired", "to", "toe", "together", 
    "tomorrow", "tongue", "tooth", "top", "touch", "town", "trade", "train", "transport", "tray", "tree", "trick", "trouble", "trousers", "true", "turn", "twist", 
    "umbrella", "under", "unit", "up", "use", "value", "verse", "very", "vessel", "view", "violent", "voice", "waiting", "walk", "wall", "war", "warm", "wash", "waste", 
    "watch", "water", "wave", "wax", "way", "weather", "week", "weight", "well", "west", "wet", "wheel", "when", "where", "while", "whip", "whistle", "white", "who", 
    "why", "wide", "will", "wind", "window", "wine", "wing", "winter", "wire", "wise", "with", "woman", "wood", "wool", "word", "work", "worm", "wound", "writing", 
    "wrong", "year", "yellow", "yes", "yesterday", "you", "young", "Bernhard", "Breytenbach", "Android"

 
]

class HangmanGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.geometry("700x400")
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
