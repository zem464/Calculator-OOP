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
                again = input("More calculations? Put 'n' if none: ")
                    # Continue if there are more calculations
                if again.lower() == 'n':
                    print("Thank you!")
                    break
            
            # If input is invalid
            else:
                print("Invalid input.")

    # For 3 inputs
    elif num == '3':
        # Show operations
        print("\nIn selecting operations, pick a number.")
        print("5. +, +")
        print("6. +, -")
        print("7. +, *")
        print("8. +, /")
        print("9. -, +")
        print("10. -, -")
        print("11. -, *")
        print("12. -, /")
        print("13. *, +")
        print("14. *, -")
        print("15. *, *")
        print("16. *, /")
        print("17. /, +")
        print("18. /, -")
        print("19. /, *")
        print("20. /, /")

        # Use while loop
        while True:
            # Take the operations to be used by the users
            operations = input("\nOperation: ")

            # Check input
            if operations in ('5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'):
                # use try-except handling
                try:
                    inp_num1 = float(input("Enter number: "))
                    inp_num2 = float(input("Enter another number: "))
                    inp_num3 = float(input("Enter another number: "))
                except ValueError:
                    print("Invalid input. Please enter numbers.")
                    continue

            # If both addition
            if operations == '5':
                print(inp_num1, "+", inp_num2, "+", inp_num3, "=", calculate.add(inp_num1, inp_num2) + inp_num3)
            
            # If addition and subtraction
            elif operations == '6':
                print(inp_num1, "+", inp_num2, "-", inp_num3, "=", calculate.add(inp_num1, inp_num2) - inp_num3)

            # If addition and multiplication
            elif operations == '7':
                print(inp_num1, "+", inp_num2, "*", inp_num3, "=", calculate.add(inp_num1, inp_num2) * inp_num3)

            # If addition and division
            elif operations == '8':
                try:
                    print(inp_num1, "+", inp_num2, "/", inp_num3, "=", calculate.add(inp_num1, inp_num2) / inp_num3)
                except ZeroDivisionError:
                    print("Cannot divide by zero")
            
            # If subtraction and addition
            elif operations == '9':
                print(inp_num1, "-", inp_num2, "+", inp_num3, "=", calculate.subtract(inp_num1, inp_num2) + inp_num3)
            
            # If both subtraction
            elif operations == '10':
                print(inp_num1, "-", inp_num2, "-", inp_num3, "=", calculate.subtract(inp_num1, inp_num2) - inp_num3)

            # If subtraction and multiplication
            elif operations == '11':
                print(inp_num1, "-", inp_num2, "*", inp_num3, "=", calculate.subtract(inp_num1, inp_num2) * inp_num3)

            # If subtraction and division
            elif operations == '12':
                try:
                    print(inp_num1, "-", inp_num2, "/", inp_num3, "=", calculate.subtract(inp_num1, inp_num2) / inp_num3)
                except ZeroDivisionError:
                    print("Cannot divide by zero")
            
            # If multiplication and addition
            elif operations == '13':
                print(inp_num1, "*", inp_num2, "+", inp_num3, "=", calculate.multiply(inp_num1, inp_num2) + inp_num3)
            
            # If multiplication and subtraction
            elif operations == '14':
                print(inp_num1, "*", inp_num2, "-", inp_num3, "=", calculate.multiply(inp_num1, inp_num2) - inp_num3)

            # If both multiplication
            elif operations == '15':
                print(inp_num1, "*", inp_num2, "*", inp_num3, "=", calculate.multiply(inp_num1, inp_num2) * inp_num3)

            # If multiplication and division
            elif operations == '16':
                try:
                    print(inp_num1, "*", inp_num2, "/", inp_num3, "=", calculate.multiply(inp_num1, inp_num2) / inp_num3)
                except ZeroDivisionError:
                    print("Cannot divide by zero")

            # If division and addition
            elif operations == '17':
                try:
                    print(inp_num1, "/", inp_num2, "+", inp_num3, "=", calculate.divide(inp_num1, inp_num2) + inp_num3)
                except ZeroDivisionError:
                    print("Cannot divide by zero")

            # If division and subtraction
            elif operations == '18':
                try:
                    print(inp_num1, "/", inp_num2, "-", inp_num3, "=", calculate.divide(inp_num1, inp_num2) - inp_num3)
                except ZeroDivisionError:
                    print("Cannot divide by zero")

            # If division and multiplication
            elif operations == '19':
                try:
                    print(inp_num1, "/", inp_num2, "*", inp_num3, "=", calculate.divide(inp_num1, inp_num2) * inp_num3)
                except ZeroDivisionError:
                    print("Cannot divide by zero")

            # If both division
            elif operations == '20':
                try:
                    print(inp_num1, "/", inp_num2, "/", inp_num3, "=", calculate.divide(inp_num1, inp_num2) / inp_num3)
                except ZeroDivisionError:
                    print("Cannot divide by zero")

            # Ask for more calculations
            again = input("More calculations? Put 'n' if none: ")
                # Break if no other calculations
            if again.lower() == 'n':
                print("Thank you!")
                break

            # If input is invalid
            else:
                print("Invalid input.")

    # Give choices, if input is not in the choices
    else:
        print("Please enter 2 or 3 only.")

except ValueError:
    print("You can only put integers.")