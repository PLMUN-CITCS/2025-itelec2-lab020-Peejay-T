def get_integer_input():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    else:
        return f"{number} is an Odd number."

# Main Program Flow
num = get_integer_input()  # Get user input
result = check_even_odd(num)  # Check if it's even or odd
print(result)  # Display the result
