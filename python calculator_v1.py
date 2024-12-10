help = input("Welcome to bot calculator. For help, enter /help:\n")
if help == "/help":
    print("Commands for calculator are [+, -, /, *, //, %]")

def calculator():
    number_first = float(input("Enter the first number for calculator:\n"))
    number_second = float(input("Enter the second number for calculator:\n"))
    operation = input("Enter operation for calculator:\n")

    if operation == "+":
        print(f"Result: {number_first + number_second}")
    elif operation == "-":
        print(f"Result: {number_first - number_second}")
    elif operation == "/":
        if number_second == 0:
            print("You can't divide by zero!")
        else:
            print(f"Result: {number_first / number_second}")
    elif operation == "*":
        print(f"Result: {number_first * number_second}")
    elif operation == "//":
        if number_second == 0:
            print("You can't divide by zero!")
        else:
            print(f"Result: {number_first // number_second}")
    elif operation == "%":
        if number_second == 0:
            print("You can't divide by zero!")
        else:
            print(f"Result: {number_first % number_second}")
    else:
        print("Invalid operation. Please try again.")

while True:
    calculator()
    choice = input("Do you want to calculate again? (yes/no):\n").strip().lower()
    if choice != "yes":
        print("Goodbye!")
        break