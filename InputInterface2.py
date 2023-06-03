# Interface for 2-inputs

# Create class
class input2:
    def operations_display_for2(self):
        # Show operations
        print("\n\033[33;40m\033[1mIn selecting operations, pick a number.\033[0m")
        print("1. +\n2. -\n3. *\n4. /")

    def print_sum(self, sum):
        print("=", str(sum))

    def print_subtract(self, difference):
        print("=", str(difference))

    def print_multiply(self, product):
        print("=", str(product))

    def print_divide(self, quotient):
        print("=", str(quotient))

    def not_an_option(self):
        print("\033[31m\033[1mPick only from 1 to 4")