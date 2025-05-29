# A poorly written example of a program in Python. It prompts the user for the number of elements to sum, takes those integers as input, and handles some basic error cases

MAX_ELEMENTS = 100

def calculate_sum(numbers):
    """Return the sum of a list of integers."""
    return sum(numbers)

def get_number_of_elements():
    """Prompt the user for the number of elements and validate input."""
    while True:
        try:
            n = int(input(f"Enter the number of elements (1-{MAX_ELEMENTS}): "))
            if 1 <= n <= MAX_ELEMENTS:
                return n
            print(f"Invalid input. Please enter a number between 1 and {MAX_ELEMENTS}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def get_numbers(n):
    """Prompt the user to enter n integers and validate input."""
    numbers = []
    print(f"Enter {n} integers:")
    while len(numbers) < n:
        try:
            num = int(input())
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    return numbers

def main():
    try:
        n = get_number_of_elements()
        numbers = get_numbers(n)
        total = calculate_sum(numbers)
        print("Sum of the numbers:", total)
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")

if __name__ == "__main__":
    main()
