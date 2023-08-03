# Importing necessary functions from the itertools module
from itertools import permutations, product

# Defining a function to find equations using four numbers that evaluate to 10
def four_equal_10(numbers):
    # Creating an empty set to store unique solutions
    solutions = set()
    
    # List of arithmetic operators
    operators = ["+", "-", "/", "*"]
    
    # Generating permutations of the given numbers
    for nums in permutations(numbers):
        # Generating combinations of operators with repetition
        for ops in product(operators, repeat=3):
            # Constructing the equation string using numbers and operators
            equation = f"{nums[0]} {ops[0]} {nums[1]} {ops[1]} ({nums[2]} {ops[2]} {nums[3]})"
            
            try:
                # Evaluating the equation and checking if it equals 10
                if eval(equation) == 10 and equation not in solutions:
                    # Adding valid solutions to the set
                    solutions.add(equation)
            except ZeroDivisionError:
                # Handling division by zero errors
                pass
    
    # Returning the set of solutions
    return solutions

# Main loop
while True:
    # Taking user input for four numbers or the option to quit
    input_string = input("Enter 4 numbers (or quit/exit to Exit):")
    
    # Checking if the user wants to quit
    if input_string.lower() == "quit" or input_string.lower() == "exit":
        break
    
    try:
        # Converting the input string into a list of integers
        numbers = list(map(int, input_string.split()))
        
        # Checking if exactly four numbers were entered
        if len(numbers) != 4:
            print("Enter four numbers exactly!")
            continue
        
        # Calling the function to find solutions using the entered numbers
        solutions = four_equal_10(numbers)
        
        if solutions:
            print(len(solutions) ,"solutions found:")
            # Displaying the solutions
            for idx, solution in enumerate(solutions):
                print(str(idx+1) + ". ", solution)
        else:
            print("No solution found.")
    
    except ValueError:
        # Handling invalid input (non-integer values)
        print("Invalid input. Enter valid numbers.")
