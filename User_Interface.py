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
    
    def operations_display_for2(self):
        # Show operations
        print("\n\033[33;40m\033[1mIn selecting operations, pick a number.\033[0m")
        print("1. +\n2. -\n3. *\n4. /")
    
    def operations_ask(self):
        # Take operation to be used
        operations = input("\n\033[34m\033[1mOperation: \033[37m\033[0m")
        return operations
    
    def input_num(self):
        try:
            inp_num = float(input("\033[34m\033[1mEnter number: \033[37m\033[0m"))
            return inp_num
        except ValueError:
            print("\033[31m\033[1mInvalid input. Please enter numbers.")
            return self.input_num()
    
    def print_sum(self, sum):
        print("=", str(sum))

    def print_subtract(self, difference):
        print("=", str(difference))

    def print_multiply(self, product):
        print("=", str(product))

    def print_divide(self, quotient):
        print("=", str(quotient))
    
    def for_ZeroDiv(self):
        print("\033[31m\033[1mCannot divide by zero")
    
    def ask_again(self):
        input("More calculations? Put 'n' if none: \n".lower())
    
    def no_more(self):
        print("\n\033[35m\033[1mThank you!")
    
    def not_operation(self):
        print("\033[31m\033[1mInvalid input.")
    
    def operations_display_for3(self):
        # Show operations
        print("\n\033[33;40m\033[1mIn selecting operations, pick a number.\033[0m")
        print("5. +, +\n6. +, -\n7. +, *\n8. +, /\n9. -, +\n10. -, -")
        print("11. -, *\n12. -, /\n13. *, +\n14. *, -\n15. *, *\n16. *, /")
        print("17. /, +\n18. /, -\n19. /, *\n20. /, /")

    def not_inputsNum(self):
        print("\033[31m\033[1mPlease enter 2 or 3 only.")

    def print_add_add(self, add_add):
        print("=", str(add_add))
    
    def print_add_sub(self, add_sub):
        print("=", str(add_sub))
    
    def print_add_multi(self, add_multi):
        print("=", str(add_multi))
    
    def print_add_div(self, add_div):
        print("=", str(add_div))
    
    def print_sub_add(self, sub_add):
        print("=", str(sub_add))
    
    def print_sub_sub(self, sub_sub):
        print("=", str(sub_sub))
    
    def print_sub_multi(self, sub_multi):
        print("=", str(sub_multi))
    
    def print_sub_div(self, sub_div):
        print("=", str(sub_div))

    def print_multi_add(self, multi_add):
        print("=", str(multi_add))
    
    def print_multi_sub(self, multi_sub):
        print("=", str(multi_sub))
    
    def print_multi_multi(self, multi_multi):
        print("=", str(multi_multi))
    
    def print_multi_div(self, multi_div):
        print("=", str(multi_div))
    
    def print_div_add(self, div_add):
        print("=", str(div_add))
    
    def print_div_sub(self, div_sub):
        print("=", str(div_sub))
    
    def print_div_multi(self, div_multi):
        print("=", str(div_multi))
    
    def print_div_div(self, div_div):
        print("=", str(div_div))