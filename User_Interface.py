# Create or move the methods from the main program

class UserInterface:
    def greetings(self):
        # Print the intro or greetings
        print("==========================================================================")
        print("|\033[37;40m                          " + "\033[35;40m\033[1mSIMPLE CALCULATOR\033[0m" + "\033[37;40m                             \033[37m|")
        print("==========================================================================" + "\n")
    
    def ask_inputsNum(self):
        # Ask how many numbers are to be calculated
        print("\033[33m**Note that this calculator can only except no more than 3 inputs.\n")
        num = input("\033[34m\033[1mHow many numbers will you input?: \033[37m\033[0m")
        return num

    def operations_ask(self):
        # Take operation to be used
        operations = input("\n\033[34m\033[1mOperation: \033[37m\033[0m")
        return operations
    
    def input_num(self):
        # Ask the user for an input
        try:
            inp_num = float(input("\033[34m\033[1mEnter number: \033[37m\033[0m"))
            return inp_num
        except ValueError:
            print("\033[31m\033[1mInvalid input. Please enter numbers.")
            return self.input_num()
    
    def for_ZeroDiv(self):
        # Displayed on ZeroDivisionError
        print("\033[31m\033[1mCannot divide by zero")
    
    def ask_again(self):
        # Asking if there are more calculations
        again = input("\n\033[32m\033[1mMore calculations? Put 'n' if none: \033[37m\033[0m")
        if again.lower() == 'n':
            return True
    
    def no_more(self):
        # Closing greetings if no calculations
        print("\n\033[35m\033[1mThank you!")
    
    def not_operation(self):
        # Display if the operation is not an integer
        print("\033[31m\033[1mInvalid input.")

    def not_inputsNum(self):
        # Display if the number for inputs are neither 2 nor 3
        print("\033[31m\033[1mPlease enter 2 or 3 only.")