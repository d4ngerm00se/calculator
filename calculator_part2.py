# Create a function to convert a text file into a list of equations
def read_equations(file_name):
    '''
    This function reads equations from a file and returns them as a list of strings. It takes a single parameter file_name, which is a string representing the name of the file to be read.

    The function initializes an empty list called equations and attempts to open the specified file using a with statement. It reads the file line by line, strips any leading or trailing whitespace using the strip() method, and appends the resulting string to the equations list.

    If the file specified by file_name cannot be found, the function prints an error message and returns an empty list. If the file is successfully read, the function returns a list of strings representing the equations contained in the file.

    :param file_name: a string representing the name of the file to be read
    :type file_name: str
    :return: a list of strings representing the equations contained in the file
    :rtype: list
    '''
    equations = []
    try:
        with open(file_name, 'r') as file:
            for line in file:
                equations.append(line.strip())
    except FileNotFoundError:
        print(f"File {file_name} not found. Please try again; remember to add .txt!")
    return equations

# Create a calculator that takes in two numbers and an operator and returns the result
def calculate(no1, no2, operator):
    if operator == "+":
        return no1 + no2
    elif operator == "*":
        return no1 * no2
    elif operator == "-":
        return no1 - no2
    elif operator == "/":
        if no2 == 0:
            print("You cannot divide by zero!")
        else:
            return no1 / no2
    elif operator == "%":
        return no1 % no2
    elif operator == "**":
        try:
            return no1 ** no2
        except OverflowError:
            print("Your numbers are too big!")
    else:
        return None

# Specifying a txt file to append the results to if Choice 1   
equations_file = open("equations.txt", "a")  

choice = input("Please enter 1 to enter two numbers and an operator, or 2 to read equations from a file: ")

if choice == "1":
    # Using a while loop to make the calculator reusable
    while True:
        # Taking user inputs and ensuring program doesn't break if non-numerical characters provided
        try:
            no1 = float(input("Please enter your first number: "))
            no2 = float(input("Please enter your second number: "))
        except ValueError:
            print("You did not enter valid numbers. Please try again.")
            continue
        operator = input("Please enter a valid operator (+, -, *, /, %, **): ")

        result = calculate(no1, no2, operator)

        # Printing the result and adding to txt file if valid, error message otherwise
        if result is not None:
            equation = f"{no1} {operator} {no2} = {result}"
            print(equation)
            equations_file.write(equation + "\n")
        elif result == None and no2 == 0:
            pass
        else:
            print("You did not enter a valid operator. Please try again.")

        # Asking user if they wish to perform another calculation
        go_on = input("Do you wish to calculate another equation? Type y for yes, anything else for no: ")
        if go_on.lower() != "y" :
            break

    print("Thank you for using the calculator. Goodbye!")

elif choice == "2":
    # Asking user for name of file, passing through function to convert to list of equations, performing calculations
    file_name = input("Enter the file name: ")
    equations = read_equations(file_name)
    for equation in equations:
        try:
            result = eval(equation)
            print(f"{equation} = {result}")
        except (SyntaxError, TypeError, NameError, OverflowError):
            print(f"Invalid expression: {equation}")