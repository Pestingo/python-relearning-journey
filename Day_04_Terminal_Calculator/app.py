# Day 04 Project: Command-Line Terminal Calculator

print("🖥️  Interactive Terminal Calculator Initialized.")
print("Type 'exit' at any prompt to close the application.\n")

while True:
    print("--- New Calculation ---")
    
    # 1. Capture user choice for operations
    operation = input("Choose operation (+, -, *, /) or type 'exit': ").strip()
    
    # Check for break condition
    if operation.lower() == 'exit':
        print("🔌 Shutting down calculator. Goodbye!")
        break
        
    if operation not in ['+', '-', '*', '/']:
        print("❌ Invalid operator selection. Please try again.\n")
        continue

    # 2. Capture and typecast numeric inputs safely
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("❌ System Error: Invalid numeric input. Please enter numbers only.\n")
        continue

    # 3. Process structural evaluations (if-elif-else execution blocks)
    if operation == '+':=
        result = num1 + num2
        print(f"📊 Result: {num1} + {num2} = {result}\n")
    elif operation == '-':
        result = num1 - num2
        print(f"📊 Result: {num1} - {num2} = {result}\n")
    elif operation == '*':
        result = num1 * num2
        print(f"📊 Result: {num1} * {num2} = {result}\n")
    elif operation == '/':
        # Edge case check: Avoid dividing by zero crashes
        if num2 == 0:
            print("⚠️ Math Error: Division by zero is undefined.\n")
        else:
            result = num1 / num2
            print(f"📊 Result: {num1} / {num2} = {result}\n")