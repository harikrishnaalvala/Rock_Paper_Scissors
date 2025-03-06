import random

# Winning rules of the game
WINNING_RULES = {
    ("Rock", "Paper"): "Paper",
    ("Rock", "Scissors"): "Rock",
    ("Paper", "Scissors"): "Scissors"
}

CHOICES = {1: "Rock", 2: "Paper", 3: "Scissors"}

print("Winning rules of Rock Paper Scissors:")
print("Rock vs Paper -> Paper wins")
print("Rock vs Scissors -> Rock wins")
print("Paper vs Scissors -> Scissors wins\n")

while True:
    try:
        # Take user input
        print("Enter your choice:\n 1 - Rock \n 2 - Paper \n 3 - Scissors")
        choice = int(input("Enter your choice: "))

        # Validate input
        if choice not in CHOICES:
            print("Invalid choice! Please enter 1, 2, or 3.\n")
            continue

        user_choice = CHOICES[choice]
        print(f"User choice is: {user_choice}")

        # Computer's turn
        comp_choice = CHOICES[random.randint(1, 3)]
        print(f"Computer choice is: {comp_choice}")

        # Determine the winner
        if user_choice == comp_choice:
            print("<== It's a tie! ==>")
        elif (user_choice, comp_choice) in WINNING_RULES:
            print(f"<== {WINNING_RULES[(user_choice, comp_choice)]} wins! ==>")
            print("<== User wins! ==>") if WINNING_RULES[(user_choice, comp_choice)] == user_choice else print("<== Computer wins! ==>")
        else:
            print(f"<== {WINNING_RULES[(comp_choice, user_choice)]} wins! ==>")
            print("<== User wins! ==>") if WINNING_RULES[(comp_choice, user_choice)] == user_choice else print("<== Computer wins! ==>")

        # Ask if the user wants to play again
        play_again = input("\nDo you want to play again? (Y/N): ").strip().lower()
        if play_again != 'y':
            break

    except ValueError:
        print("Invalid input! Please enter a number (1, 2, or 3).\n")

print("Thanks for playing!")
