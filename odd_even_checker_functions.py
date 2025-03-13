def get_integer_input(prompt: str) -> int:
    """
    Prompts the user for an integer input and validates the input.
    
    Args:
        prompt (str): The message displayed to the user.
    
    Returns:
        int: A valid integer input from the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    Determines whether a given number is even or odd.
    
    Args:
        number (int): The number to check.
    
    Returns:
        str: A message stating whether the number is even or odd.
    """
    return f"{number} is an Even number." if number % 2 == 0 else f"{number} is an Odd number."

# Main program execution
if __name__ == "__main__":
    user_number = get_integer_input("Enter an integer: ")
    result = check_even_odd(user_number)
    print(result)
