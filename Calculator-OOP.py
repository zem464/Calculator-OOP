# Import the class
from User_Interface import UserInterface
from Calcu_Class import calculator

# Create the object
ui = UserInterface()
calculate = calculator()

# Print the intro or greetings
ui.greetings()

# Ask how many numbers are to be calculated
num = ui.ask_inputsNum()

# For 2 inputs
if num == '2':
        # Show operations
        ui.operations_display()

        # Use while loop
        while True:
            # Take operation to be used
            operations = ui.operations_ask()

            # Check input
            if operations in ('1', '2', '3', '4'):
                inp_num1 = ui.input_num()
                inp_num2 = ui.input_num()

                # If addition
                if operations == '1':
                    sum = calculate.add(inp_num1, inp_num2)
                    ui.print_sum(sum)
                    
                # If subtraction
                elif operations == '2':
                    difference = calculate.subtract(num1, num2)
                    ui.print_subtract(difference)

                # If multiplication
                elif operations == '3':
                    product = calculate.multiply(num1, num2)
                    ui.print_multiply(product)

                # If division
                elif operations == '4':
                    quotient = calculate.divide(num1, num2)
                    ui.print_divide(quotient)

                # Ask for more calculations
                ask = ui.ask_again()
                if ask == 'n':
                    ui.no_more()
                break
        
        # If input is invalid
        else:
            ui.not_operation()

# For 3 inputs
elif num == '3':
    # Show operations
    print("\n\033[33;40m\033[1mIn selecting operations, pick a number.\033[0m")
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
        operations = input("\n\033[34m\033[1mOperation: \033[37m\033[0m")

        # Check input
        if operations in ('5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'):
            # use try-except handling
            try:
                inp_num1 = float(input("\033[34m\033[1mEnter number: \033[37m\033[0m"))
                inp_num2 = float(input("\033[34m\033[1mEnter another number: \033[37m\033[0m"))
                inp_num3 = float(input("\033[34m\033[1mEnter another number: \033[37m\033[0m"))
            except ValueError:
                print("\033[31m\033[1mInvalid input. Please enter numbers.")
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
                print("\033[31m\033[1mCannot divide by zero")
        
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
                print("\033[31m\033[1mCannot divide by zero")
        
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
                print("\033[31m\033[1mCannot divide by zero")

        # If division and addition
        elif operations == '17':
            try:
                print(inp_num1, "/", inp_num2, "+", inp_num3, "=", calculate.divide(inp_num1, inp_num2) + inp_num3)
            except ZeroDivisionError:
                print("\033[31m\033[1mCannot divide by zero")

        # If division and subtraction
        elif operations == '18':
            try:
                print(inp_num1, "/", inp_num2, "-", inp_num3, "=", calculate.divide(inp_num1, inp_num2) - inp_num3)
            except ZeroDivisionError:
                print("\033[31m\033[1mCannot divide by zero")

        # If division and multiplication
        elif operations == '19':
            try:
                print(inp_num1, "/", inp_num2, "*", inp_num3, "=", calculate.divide(inp_num1, inp_num2) * inp_num3)
            except ZeroDivisionError:
                print("\033[31m\033[1mCannot divide by zero")

        # If both division
        elif operations == '20':
            try:
                print(inp_num1, "/", inp_num2, "/", inp_num3, "=", calculate.divide(inp_num1, inp_num2) / inp_num3)
            except ZeroDivisionError:
                print("\033[31m\033[1mCannot divide by zero")

        # Ask for more calculations
        again = input("\n\033[32m\033[1mMore calculations? Put 'n' if none: \033[37m\033[0m")
            # Break if no other calculations
        if again.lower() == 'n':
            print("\n\033[35m\033[1mThank you!")
            break

    # If input is invalid
    else:
        print("\033[31m\033[1mInvalid input.")

# Give choices, if input is not in the choices
else:
    print("\033[31m\033[1mPlease enter 2 or 3 only.")