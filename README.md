# Guess the Number Game

This is a simple guess the number game written in Python. The computer randomly selects a number between 1 and 100, and the player tries to guess the number. The computer provides hints whether the guess is too high, too low, or correct.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TamerAlaeddin/guess-the-number.git
   cd guess-the-number
   ```

2. **Run the application:**
   ```bash
   python guess_the_number.py
   ```

## Features

- **Random Number Generation**: The computer selects a random number between 1 and 100.
- **User Input Handling**: The player enters a guess.
- **Hints**: The game provides hints if the guess is too high or too low.
- **Congratulatory Message**: The game congratulates the player when they guess the number correctly and displays the number of attempts.
- **Input Validation**: The game handles invalid inputs and prompts the player to enter a valid number.

## Usage

1. **Run the program**: When you run the program, you will be prompted to guess a number between 1 and 100:
   ```
   Welcome to the guessing game! 
   Please guess a number between (1-100) to play. 
   
   Guess your number: 
   ```

2. **Enter your guess**: Enter a number between 1 and 100.

3. **Receive feedback**: The game will provide feedback:
   - "Too Low!" if your guess is lower than the number.
   - "Too High!" if your guess is higher than the number.
   - "Congratulations, You guessed the number in X attempts!" if your guess is correct.

4. **Invalid input**: If you enter a non-numeric value, the game will prompt you to enter a valid number.

## Example

```
Welcome to the guessing game! 
Please guess a number between (1-100) to play. 

Guess your number: 50
Too Low!
Guess your number: 75
Too High!
Guess your number: 60
Congratulations, You guessed the number in 3 attempts!
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.