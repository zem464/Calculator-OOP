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

                # If addition

                # If subtraction

                # If multiplication

                # If division

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