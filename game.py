import random

# Step 1: Ask for user's name
name = input("Enter your name: ")
print(f"Hello, {name}")

# Step 2: Load initial score from rating.txt
score = 0
try:
    with open("rating.txt", "r", encoding="utf-8") as file:
        for line in file:
            user, points = line.strip().split()
            if user == name:
                score = int(points)
                break
except FileNotFoundError:
    pass

# Step 3: Read game options
options_input = input()
options = options_input.split(",") if options_input else ["rock", "paper", "scissors"]
print("Okay, let's start")

# Helper: who wins
def determine_result(user, computer, options):
    if user == computer:
        return "draw"
    
    half = len(options) // 2
    user_index = options.index(user)
    # Wrap around list for circular behavior
    rotated = options[user_index + 1:] + options[:user_index]
    beats_user = rotated[:half]
    
    if computer in beats_user:
        return "loss"
    else:
        return "win"

# Step 4: Game loop
while True:
    user_choice = input()

    if user_choice == "!exit":
        print("Bye!")
        break
    elif user_choice == "!rating":
        print(f"Your rating: {score}")
    elif user_choice not in options:
        print("Invalid input")
    else:
        computer_choice = random.choice(options)
        result = determine_result(user_choice, computer_choice, options)

        if result == "draw":
            print(f"There is a draw ({computer_choice})")
            score += 50
        elif result == "win":
            print(f"Well done. The computer chose {computer_choice} and failed")
            score += 100
        else:
            print(f"Sorry, but the computer chose {computer_choice}")
