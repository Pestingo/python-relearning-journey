# Day 05 Project: Perfected Random Number Guessing Game
import random

# Initialize the application state
secret_number = random.randint(1, 100)
attempts = 0

print("=========================================")
print("🎮 Welcome to the Number Guessing Game!")
print("=========================================")
print("I have chosen a secret number between 1 and 100.")
print("Can you decode it? Let's find out.\n")

while True:
    # 1. Capture stream input and clean trailing spaces
    user_input = input("Enter your guess (or type 'quit' to exit): ").strip()
    
    # 2. Check for explicit exit command
    if user_input.lower() == 'quit':
        print(f"🔌 Operational Shutdown: You gave up! The secret number was {secret_number}.")
        break
        
    # 3. Dynamic exception handling & evaluation validation
    try:
        guess = int(user_input)
    except ValueError:
        print("❌ Validation Error: Please enter a valid whole number.\n")
        continue
    
    # Only increment attempts if the input was a valid integer
    attempts += 1

    # 4. Binary evaluation conditions
    if guess == secret_number:
        print(f"\n🎉 Congratulations! You guessed the secret number in {attempts} attempts!")
        break
    elif guess < secret_number:
        print("📉 Too low! Try a higher number.\n")
    else:
        print("📈 Too high! Try a lower number.\n")