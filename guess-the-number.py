import random

def main():
    number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the guessing game! \nPlease guess a number between (1-100) to play. \n")

    while True:
        try:
            guess = int(input("Guess your number: "))
            attempts += 1
            
            if guess < number:
                print("Too Low!")
            elif guess > number:
                print("Too High!")
            else:
                print(f"\nCongratulations, You guess the number in {attempts} attempts!")
                break
        except ValueError:
            print("\nInvalid input. PLease enter a number.")       
            
if __name__ == "__main__":
    main()