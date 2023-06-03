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
    
    def operations_display(self):
        # Show operations
        print("\n\033[33;40m\033[1mIn selecting operations, pick a number.\033[0m")
        print("1. +\n 2. - \n 3. * \n 4. / \n")
    
    def operations_ask(self):
        # Take operation to be used
        operations = input("\n\033[34m\033[1mOperation: \033[37m\033[0m")
        return operations
    
    def input_num(self):
        try:
            inp_num = float(input("\033[34m\033[1mEnter number: \033[37m\033[0m"))
        except ValueError:
            print("\033[31m\033[1mInvalid input. Please enter numbers.")
            return inp_num
    
    def ask_again(self):
        again = input("More calculations? Put 'n' if none: \n")
        if again.lower() == 'n':
            print("\n\033[35m\033[1mThank you!")
            return False
    
    def not_operation(self):
        print("\033[31m\033[1mInvalid input.")