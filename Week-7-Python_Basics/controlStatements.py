import random

def main():
    print("=== Number Guessing Game ===")
    secret = random.randint(1, 20)
    max_attempts = 5
    attempts = 0

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Guess a number between 1 and 20: "))
        except ValueError:
            print("Please enter a valid number.")
            continue  # Skip to next loop iteration

        if guess < 1 or guess > 20:
            print("Out of range! Guess between 1 and 20.")
            continue

        attempts += 1

        if guess == secret:
            print("🎉 Correct! You guessed the number.")
            break
        elif guess < secret:
            print("Too low!")
        else:
            print("Too high!")

        # Example of pass
        if guess == -1:
            pass  # Placeholder, does nothing

    else:
        print(f"❌ Out of attempts! The correct number was {secret}")

    print("\n--- Game Over ---")

    # Bonus: for loop example - Countdown
    print("\nRestarting in:")
    for i in range(3, 0, -1):
        print(i)

if __name__ == "__main__":
    main()
