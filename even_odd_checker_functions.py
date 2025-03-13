def get_integer_input():
    while True:
        try:
            return int(input("Enter an integer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def check_even_odd(number):
    if number % 2 == 0:
        return f"{number} is an Even number."
    elif:
        return f"{number} is an Odd number."

num = get_integer_input() 
print(check_even_odd(num))
