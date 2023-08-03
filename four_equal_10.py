from itertools import permutations, product

def four_equal_10(numbers):

    solutions = set()
    operators = ["+", "-", "/", "*"]
    

    for nums in permutations(numbers):
        for ops in product(operators, repeat = 3):

            equation = f"{nums[0]} {ops[0]} {nums[1]} {ops[1]} ({nums[2]} {ops[2]} {nums[3]})"

            try:    
                if eval(equation) == 10 and equation not in solutions:
                    solutions.add(equation)
                    
            except ZeroDivisionError:
                pass

    return solutions


while True:

    input_string = input("Enter 4 numbers (or quit/exit to Exit):")
    
    if input_string.lower() == "quit" or input_string.lower() == "exit":
        break

    try:
        numbers = list(map(int, input_string.split()))

        if len(numbers) != 4:
            print("Enter four numbers exactly!")
            continue

        solutions = four_equal_10(numbers)

        if solutions:
            print("Solutions found:")
            for idx, solution in enumerate(solutions):
                print(str(idx)+". ", solution)
        else:
            print("No solution found.")

    except ValueError:
        print("Invalid input. Enter valid numbers.")