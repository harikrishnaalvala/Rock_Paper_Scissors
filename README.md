# Rock Paper Scissors Game

## Introduction
This is a simple **Rock Paper Scissors** game implemented in Python. The user plays against the computer, selecting one of the three choices, and the game determines the winner based on the standard rules.

## Rules
- **Rock vs Paper** → Paper wins
- **Rock vs Scissors** → Rock wins
- **Paper vs Scissors** → Scissors wins
- If both the user and the computer choose the same option, it's a tie.

## How to Play
1. Run the Python script.
2. Choose one of the following options:
   - `1` for Rock
   - `2` for Paper
   - `3` for Scissors
3. The computer will randomly select its choice.
4. The winner will be determined based on the rules above.
5. You will be asked if you want to play again.
   - Enter `Y` or `y` to continue playing.
   - Enter `N` or `n` to exit the game.

## Features
✅ **User input validation** - Ensures users enter only valid choices (1, 2, or 3).  
✅ **Random computer selection** - Uses Python's `random` module.  
✅ **Clean and readable output** - Displays results clearly.  
✅ **Loop for replay** - Allows users to play multiple rounds.  

## Requirements
- Python 3.x

## How to Run the Game
1. Ensure you have Python installed.
2. Copy the script into a Python file (e.g., `rock_paper_scissors.py`).
3. Open a terminal or command prompt and navigate to the script's directory.
4. Run the script using:
   ```sh
   python rock_paper_scissors.py
   ```

## Example Output
```
Winning rules of Rock Paper Scissors:
Rock vs Paper -> Paper wins
Rock vs Scissors -> Rock wins
Paper vs Scissors -> Scissors wins

Enter your choice:
 1 - Rock
 2 - Paper
 3 - Scissors
Enter your choice: 1
User choice is: Rock
Computer choice is: Scissors
<== Rock wins! ==>
<== User wins! ==>

Do you want to play again? (Y/N): n
Thanks for playing!
```

## License
This game is free to use and modify for educational and personal purposes.

