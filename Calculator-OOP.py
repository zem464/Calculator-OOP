# Import the class
from User_Interface import UserInterface
from Calcu_Class import calculator
from Calcu_Class2 import more_ope

# Create the object
ui = UserInterface()
calculate = calculator()
calc = more_ope()

# Print the intro or greetings
ui.greetings()

# Ask how many numbers are to be calculated
num = ui.ask_inputsNum()

# For 2 inputs
if num == '2':
        # Show operations
        ui.operations_display_for2()

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
                    difference = calculate.subtract(inp_num1, inp_num2)
                    ui.print_subtract(difference)

                # If multiplication
                elif operations == '3':
                    product = calculate.multiply(inp_num1, inp_num2)
                    ui.print_multiply(product)

                # If division
                elif operations == '4':
                    try:
                        quotient = calculate.divide(inp_num1, inp_num2)
                        ui.print_divide(quotient)
                    except ZeroDivisionError:
                        ui.for_ZeroDiv()

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
    ui.operations_display_for3()

    # Use while loop
    while True:
        # Take the operations to be used by the users
        operations = ui.operations_ask()

        # Check input
        if operations in ('5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'):
            # use try-except handling
            inp_num1 = ui.input_num()
            inp_num2 = ui.input_num()
            inp_num3 = ui.input_num()

            # If both addition
            if operations == '5':
                add_add = calc.add_add(inp_num1, inp_num2, inp_num3)
                ui.print_add_add(add_add)
            
            # If addition and subtraction
            elif operations == '6':
                difference = calculate.add(inp_num1, inp_num2) - inp_num3
                ui.print_subtract(difference)

            # If addition and multiplication
            elif operations == '7':
                product = calculate.add(inp_num1, inp_num2) * inp_num3
                ui.print_multiply(product)

            # If addition and division
            elif operations == '8':
                try:
                    quotient = calculate.add(inp_num1, inp_num2) / inp_num3
                    ui.print_divide(quotient)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()
            
            # If subtraction and addition
            elif operations == '9':
                sum = calculate.subtract(inp_num1, inp_num2) + inp_num3
                ui.print_sum(sum)

            # If both subtraction
            elif operations == '10':
                difference = calculate.subtract(inp_num1, inp_num2) - inp_num3
                ui.print_subtract(difference)
                
            # If subtraction and multiplication
            elif operations == '11':
                product = calculate.subtract(inp_num1, inp_num2) * inp_num3
                ui.print_multiply(product)

            # If subtraction and division
            elif operations == '12':
                try:
                    quotient = calculate.subtract(inp_num1, inp_num2) / inp_num3
                    ui.print_divide(quotient)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()
            
            # If multiplication and addition
            elif operations == '13':
                sum = calculate.multiply(inp_num1, inp_num2) + inp_num3
                ui.print_multiply(sum)

            # If multiplication and subtraction
            elif operations == '14':
                difference = calculate.multiply(inp_num1, inp_num2) - inp_num3
                ui.print_multiply(difference)

            # If both multiplication
            elif operations == '15':
                product = calculate.multiply(inp_num1, inp_num2) * inp_num3
                ui.print_multiply(product)

            # If multiplication and division
            elif operations == '16':
                try:
                    quotient = calculate.multiply(inp_num1, inp_num2) / inp_num3
                    ui.print_divide(quotient)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # If division and addition
            elif operations == '17':
                try:
                    sum = calculate.divide(inp_num1, inp_num2) + inp_num3
                    ui.print_divide(sum)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # If division and subtraction
            elif operations == '18':
                try:
                    difference = calculate.divide(inp_num1, inp_num2) - inp_num3
                    ui.print_divide(difference)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # If division and multiplication
            elif operations == '19':
                try:
                    product = calculate.divide(inp_num1, inp_num2) * inp_num3
                    ui.print_divide(product)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # If both division
            elif operations == '20':
                try:
                    quotient = calculate.divide(inp_num1, inp_num2) / inp_num3
                    ui.print_divide(quotient)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # Ask for more calculations
            again = ui.ask_again()
                # Break if no other calculations
            if again != 'n':
                ui.ask_again()
            else: 
                ui.no_more()

    # If input is invalid
    else:
        ui.not_operation()

# Give choices, if input is not in the choices
else:
    ui.not_inputsNum()