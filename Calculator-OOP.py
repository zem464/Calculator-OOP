# Import the class
from User_Interface import UserInterface
from InputInterface2 import input2
from InputInterface3 import input3
from Calcu_Class import calculator
from Calcu_Class2 import more_ope

# Create the object
ui = UserInterface()
ii2 = input2()
ii3 = input3()
calculate = calculator()
calc = more_ope()

# Print the intro or greetings
ui.greetings()

# Ask how many numbers are to be calculated
num = ui.ask_inputsNum()

# For 2 inputs
if num == '2':
        # Show operations
        ii2.operations_display_for2()

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
                    ii2.print_sum(sum)
                    
                # If subtraction
                elif operations == '2':
                    difference = calculate.subtract(inp_num1, inp_num2)
                    ii2.print_subtract(difference)

                # If multiplication
                elif operations == '3':
                    product = calculate.multiply(inp_num1, inp_num2)
                    ii2.print_multiply(product)

                # If division
                elif operations == '4':
                    try:
                        quotient = calculate.divide(inp_num1, inp_num2)
                        ii2.print_divide(quotient)
                    except ZeroDivisionError:
                        ui.for_ZeroDiv()

                # Ask for more calculations
                asking = ui.ask_again()
                if asking == True:
                    ui.no_more()
                    break
            
            # If not in the operation choices
            else:
                ii2.not_an_option()
        
        # If input is invalid
        else:
            ui.not_operation()

# For 3 inputs
elif num == '3':
    # Show operations
    ii3.operations_display_for3()

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
                ii3.print_add_add(add_add)
            
            # If addition and subtraction
            elif operations == '6':
                add_sub = calc.add_sub(inp_num1, inp_num2, inp_num3)
                ii3.print_add_sub(add_sub)

            # If addition and multiplication
            elif operations == '7':
                add_multi = calc.add_multi(inp_num1, inp_num2, inp_num3)
                ii3.print_add_multi(add_multi)

            # If addition and division
            elif operations == '8':
                try:
                    add_div = calc.add_div(inp_num1, inp_num2, inp_num3)
                    ii3.print_add_div(add_div)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()
            
            # If subtraction and addition
            elif operations == '9':
                sub_add = calc.sub_add(inp_num1, inp_num2, inp_num3)
                ii3.print_sub_add(sub_add)

            # If both subtraction
            elif operations == '10':
                sub_sub = calc.sub_sub(inp_num1, inp_num2, inp_num3)
                ii3.print_sub_sub(sub_sub)
                
            # If subtraction and multiplication
            elif operations == '11':
                sub_multi = calc.sub_multi(inp_num1, inp_num2, inp_num3)
                ii3.print_sub_multi(sub_multi)

            # If subtraction and division
            elif operations == '12':
                try:
                    sub_div = calc.sub_div(inp_num1, inp_num2, inp_num3)
                    ii3.print_sub_div(sub_div)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()
            
            # If multiplication and addition
            elif operations == '13':
                multi_add = calc.multi_add(inp_num1, inp_num2, inp_num3)
                ii3.print_multi_add(multi_add)

            # If multiplication and subtraction
            elif operations == '14':
                multi_sub = calc.multi_sub(inp_num1, inp_num2, inp_num3)
                ii3.print_multi_sub(multi_sub)

            # If both multiplication
            elif operations == '15':
                multi_multi = calc.multi_multi(inp_num1, inp_num2, inp_num3)
                ii3.print_multi_multi(multi_multi)

            # If multiplication and division
            elif operations == '16':
                try:
                    multi_div = calc.multi_div(inp_num1, inp_num2, inp_num3)
                    ii3.print_multi_div(multi_div)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # If division and addition
            elif operations == '17':
                try:
                    div_add = calc.div_add(inp_num1, inp_num2, inp_num3)
                    ii3.print_div_add(div_add)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # If division and subtraction
            elif operations == '18':
                try:
                    div_sub = calc.div_sub(inp_num1, inp_num2, inp_num3)
                    ii3.print_div_sub(div_sub)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # If division and multiplication
            elif operations == '19':
                try:
                    div_multi = calc.div_multi(inp_num1, inp_num2, inp_num3)
                    ii3.print_div_multi(div_multi)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # If both division
            elif operations == '20':
                try:
                    div_div = calc.div_div(inp_num1, inp_num2, inp_num3)
                    ii3.print_div_div(div_div)
                except ZeroDivisionError:
                    ui.for_ZeroDiv()

            # Ask for more calculations
            asking = ui.ask_again()
            if asking == True:
                ui.no_more()
                break
            
        # If not in the operation choices
        else:
            ii3.not_an_option2()

    # If input is invalid
    else:
        ui.not_operation()

# Give choices, if input is not in the choices
else:
    ui.not_inputsNum()