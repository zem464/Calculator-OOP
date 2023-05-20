# Import the class
from Calcu_Class import calculator

# Create the object
calculate = calculator()

# Print the intro or greetings
print("==========================================================================")
print("|\033[37;40m                          " + "\033[35;40m\033[1mSIMPLE CALCULATOR\033[0m" + "\033[37;40m                             \033[37m|")
print("==========================================================================" + "\n")

# Ask how many numbers are to be calculated
print("\033[33m**Note that this calculator can only except at least 3 inputs.\n")
num = input("\033[34m\033[1mHow many numbers will you input?: \033[37m\033[0m")

# Use exception handling
try:
    # For 2 inputs
    if num == '2':
            # Show operations
            print("\nIn selecting operations, pick a number.")
            print("1. +")
            print("2. -")
            print("3. *")
            print("4. /")

            # Use while loop
            while True:
                # Take operation to be used
                operations = input("\nOperation: ")

                # Check input
                if operations in ('1', '2', '3', '4'):
                    # Use try-except handling
                    try:
                        inp_num1 = float(input("Enter number: "))
                        inp_num2 = float(input("Enter another number: "))
                    except ValueError:
                        print("Invalid input. Please enter numbers.")
                        continue

                # If addition
                if operations == '1':
                        print(inp_num1, "+", inp_num2, "=", calculate.add(inp_num1, inp_num2))
                    
                # If subtraction
                elif operations == '2':
                        print(inp_num1, "-", inp_num2, "=", calculate.subtract(inp_num1, inp_num2))

                # If multiplication
                elif operations == '3':
                        print(inp_num1, "*", inp_num2, "=", calculate.multiply(inp_num1, inp_num2))

                # If division
                elif operations == '4':
                        try:
                            print(inp_num1, "/", inp_num2, "=", calculate.divide(inp_num1, inp_num2))
                        except ZeroDivisionError:
                            print("Cannot divide by zero")
                    
                # Ask for more calculations

    # For 3 inputs

        # Use while loop

        # Take operation to be used

        # Check input

        # If addition

        # If subtraction

        # If multiplication

        # If division

        # Ask for more calculations

except ValueError:
    print("You can only put integers.")